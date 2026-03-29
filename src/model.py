"""
Physiological simulation model for body recomposition.

Evidence-based formulas used:
- Mifflin-St Jeor (BMR) — Mifflin et al. 1990
- Katch-McArdle (BMR from LBM) — McArdle et al. 2010
- Deurenberg (BF% from BMI) — Deurenberg et al. 1991
- Adaptive thermogenesis — Trexler et al. 2014
- Alan Aragon muscle gain ceiling — Aragon & Schoenfeld 2020
- Forbes P-ratio (non-linear fat/lean partitioning) — Forbes 1987
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from enum import Enum

import numpy as np
import pandas as pd

from src.utils import date_range, safe_dates


class TrainingLevel(Enum):
    BEGINNER = "Beginner (< 1 yr)"
    INTERMEDIATE = "Intermediate (1-3 yr)"
    ADVANCED = "Advanced (3+ yr)"


# Maximum monthly muscle gain as % of body weight (Alan Aragon)
_MUSCLE_GAIN_CEILING: dict[TrainingLevel, float] = {
    TrainingLevel.BEGINNER: 0.015,  # 1.0-1.5%
    TrainingLevel.INTERMEDIATE: 0.0075,  # 0.5-1.0%
    TrainingLevel.ADVANCED: 0.00375,  # 0.25-0.5%
}

# Fraction of max muscle gain achievable while in caloric deficit
_DEFICIT_MUSCLE_FACTOR: dict[TrainingLevel, float] = {
    TrainingLevel.BEGINNER: 0.5,
    TrainingLevel.INTERMEDIATE: 0.3,
    TrainingLevel.ADVANCED: 0.1,
}


@dataclass
class SimulationParams:
    age: int
    height_cm: int
    initial_weight_kg: float
    sleep_hours: float
    protein_g_per_kg: float
    fat_pct: float
    calorie_delta: int
    carb_cycling: bool
    carb_cycling_high_days: int
    carb_cycling_increase_pct: float
    training_level: TrainingLevel
    training_days_per_week: int
    start_date: date
    end_date: date
    initial_bf_pct: float | None = None
    sex: str = "Male"


def _estimate_bf_pct(weight: float, height_cm: float, age: int, sex: str) -> float:
    """Estimate body fat % from BMI using Deurenberg formula."""
    bmi = weight / (height_cm / 100) ** 2
    sex_factor = 1 if sex == "Male" else 0
    bf = 1.20 * bmi + 0.23 * age - 10.8 * sex_factor - 5.4
    return max(5.0, min(45.0, bf))


def _bmr_mifflin(weight: float, height_cm: int, age: int, sex: str) -> float:
    """Mifflin-St Jeor BMR."""
    base = 10 * weight + 6.25 * height_cm - 5 * age
    return base + 5 if sex == "Male" else base - 161


def _bmr_katch_mcardle(lean_mass_kg: float) -> float:
    """Katch-McArdle BMR (requires lean body mass)."""
    return 370 + 21.6 * lean_mass_kg


def _activity_multiplier(training_days: int) -> float:
    """TDEE multiplier based on weekly training days."""
    if training_days <= 1:
        return 1.375
    if training_days <= 3:
        return 1.55
    if training_days <= 5:
        return 1.725
    return 1.9


def _adaptive_thermogenesis(day: int, initial_weight: float, current_weight: float) -> float:
    """
    Metabolic adaptation factor (Trexler et al., 2014).
    Returns a multiplier < 1.0 that reduces TDEE during sustained deficit.
    Based on ~5-15% reduction observed in literature.
    Uses fractional weight loss as the physiological driver.
    """
    weight_loss_frac = max(0.0, (initial_weight - current_weight) / initial_weight)
    if weight_loss_frac <= 0:
        return 1.0
    # Gradually ramp up adaptation over first 30 days, max ~15% reduction
    ramp = min(1.0, day / 30)
    # Adaptation maxes out at ~10% body weight loss
    adaptation = max(0.85, 1.0 - 0.15 * ramp * min(1.0, weight_loss_frac / 0.10))
    return adaptation


def _p_ratio(bf_pct: float, weight: float) -> float:
    """
    Forbes P-ratio: fraction of energy change from fat (Forbes, 1987).
    Non-linear model: dFM/dFFM = FM / 10.4 → P_fat = FM / (FM + 10.4).
    Higher body fat → more fat mobilised, less muscle lost.
    """
    fat_mass = weight * bf_pct / 100
    p_fat = fat_mass / (fat_mass + 10.4)
    return max(0.30, min(0.95, p_fat))


def _max_daily_muscle_gain(
    weight: float,
    training_level: TrainingLevel,
    protein_factor: float,
    sleep_factor: float,
    training_stimulus: float,
    surplus_ratio: float,
) -> float:
    """Daily muscle gain ceiling in kg, modulated by factors."""
    monthly_ceiling = _MUSCLE_GAIN_CEILING[training_level] * weight
    daily_ceiling = monthly_ceiling / 30

    # Modulate by protein adequacy, sleep, training, and energy availability
    effective = daily_ceiling * protein_factor * sleep_factor * training_stimulus * surplus_ratio
    return max(0.0, effective)


def _apply_carb_cycling(
    day: int,
    base_delta: int,
    carb_pct: float,
    total_intake: float,
    high_days: int,
    increase_pct: float,
) -> tuple[float, float]:
    """Apply carb cycling redistribution. Returns (daily_delta, carb_today)."""
    day_of_week = day % 7
    low_days = 7 - high_days
    carb_cal = (carb_pct / 100) * total_intake
    extra_per_high = carb_cal * (increase_pct / 100)
    if day_of_week < high_days:
        return (
            base_delta + extra_per_high,
            min(70.0, carb_pct + increase_pct),
        )
    reduction_per_low = extra_per_high * high_days / max(1, low_days)
    return (
        base_delta - reduction_per_low,
        max(10.0, carb_pct - increase_pct * high_days / max(1, low_days)),
    )


def _partition_mass_change(
    delta_mass: float,
    p_fat: float,
    max_muscle: float,
    training_level: TrainingLevel,
) -> tuple[float, float]:
    """Partition mass change into fat and lean components."""
    if delta_mass < 0:
        fat_change = delta_mass * p_fat
        lean_change = delta_mass * (1 - p_fat)
        lean_change += max_muscle * _DEFICIT_MUSCLE_FACTOR[training_level]
    else:
        muscle_gain = min(max_muscle, delta_mass * 0.6)
        fat_change = delta_mass - muscle_gain
        lean_change = muscle_gain
    return fat_change, lean_change


def simulate(params: SimulationParams) -> tuple[pd.DataFrame, dict]:
    """Run the body recomposition simulation and return results DataFrame + metadata."""
    start, end = safe_dates(params.start_date, params.end_date)
    dates = date_range(start, end)
    n_days = len(dates)

    # Initial body fat estimation
    if params.initial_bf_pct is not None:
        bf_pct_initial = params.initial_bf_pct
    else:
        bf_pct_initial = _estimate_bf_pct(
            params.initial_weight_kg, params.height_cm, params.age, params.sex
        )

    # Arrays
    weight = np.zeros(n_days)
    fat = np.zeros(n_days)
    lean = np.zeros(n_days)
    glycogen = np.zeros(n_days)
    bf_pct_arr = np.zeros(n_days)
    tdee_arr = np.zeros(n_days)

    # Initial values — glycogen is part of the user-entered weight
    glycogen[0] = 2.5  # kg (water + glycogen in muscles/liver)
    tissue_weight = params.initial_weight_kg - glycogen[0]
    fat[0] = tissue_weight * (bf_pct_initial / 100)
    lean[0] = tissue_weight * (1 - bf_pct_initial / 100)
    weight[0] = params.initial_weight_kg  # matches user input exactly
    bf_pct_arr[0] = bf_pct_initial

    # Macro split — protect against non-positive intake
    base_tdee = _bmr_mifflin(
        params.initial_weight_kg, params.height_cm, params.age, params.sex
    ) * _activity_multiplier(params.training_days_per_week)
    total_intake = max(800.0, base_tdee + params.calorie_delta)

    protein_kcal = params.protein_g_per_kg * params.initial_weight_kg * 4
    protein_pct = min(60.0, (protein_kcal / total_intake) * 100)
    fat_pct_macro = min(params.fat_pct, 100 - protein_pct - 5)
    carb_pct_macro = max(5.0, 100 - protein_pct - fat_pct_macro)

    # Factors
    sleep_factor = max(0.65, min(1.05, 1.0 - 0.12 * (7 - params.sleep_hours)))
    protein_factor = min(1.0, params.protein_g_per_kg / 2.2)
    training_stimulus = min(1.0, params.training_days_per_week / 5)

    for day in range(1, n_days):
        current_bf_pct = (
            (fat[day - 1] / weight[day - 1]) * 100 if weight[day - 1] > 0 else bf_pct_initial
        )

        # BMR: average of Mifflin-St Jeor and Katch-McArdle
        bmr_msj = _bmr_mifflin(weight[day - 1], params.height_cm, params.age, params.sex)
        bmr_km = _bmr_katch_mcardle(lean[day - 1])
        bmr = (bmr_msj + bmr_km) / 2

        # TDEE with activity and adaptive thermogenesis
        # (TEF is already implicit in standard activity multipliers)
        activity_mult = _activity_multiplier(params.training_days_per_week)
        at_mult = _adaptive_thermogenesis(day, params.initial_weight_kg, weight[day - 1])

        tdee = bmr * activity_mult * at_mult
        tdee_arr[day] = tdee

        # Calorie intake with carb cycling redistribution
        daily_delta = params.calorie_delta
        carb_today = carb_pct_macro
        if params.carb_cycling:
            daily_delta, carb_today = _apply_carb_cycling(
                day,
                params.calorie_delta,
                carb_pct_macro,
                total_intake,
                params.carb_cycling_high_days,
                params.carb_cycling_increase_pct,
            )

        intake = tdee + daily_delta

        # Energy balance
        effective_delta = intake - tdee
        delta_mass = effective_delta / 7700  # kg change

        # Partitioning (Forbes non-linear P-ratio)
        p_fat = _p_ratio(current_bf_pct, weight[day - 1])

        # Surplus ratio based on effective (not planned) delta
        surplus_ratio = 1.0
        if effective_delta > 0:
            surplus_ratio = min(1.3, 1.0 + effective_delta / 2000)
        elif effective_delta < 0:
            surplus_ratio = max(0.4, 1.0 + effective_delta / 2000)

        max_muscle = _max_daily_muscle_gain(
            weight[day - 1],
            params.training_level,
            protein_factor,
            sleep_factor,
            training_stimulus,
            surplus_ratio,
        )

        fat_change, lean_change = _partition_mass_change(
            delta_mass,
            p_fat,
            max_muscle,
            params.training_level,
        )

        fat[day] = max(0.5, fat[day - 1] + fat_change)
        lean[day] = max(lean[0] * 0.85, lean[day - 1] + lean_change)

        # Glycogen: dynamic model — smooth transition toward target
        target_glycogen = 2.5 * (carb_today / 50) * (1 - 0.3 * training_stimulus)
        glycogen[day] = glycogen[day - 1] + 0.3 * (target_glycogen - glycogen[day - 1])
        glycogen[day] = max(0.5, min(5.0, glycogen[day]))

        weight[day] = fat[day] + lean[day] + glycogen[day]
        bf_pct_arr[day] = (fat[day] / weight[day]) * 100

    tdee_arr[0] = tdee_arr[1] if n_days > 1 else 0

    df = pd.DataFrame({
        "date": dates,
        "weight": weight,
        "fat": fat,
        "lean": lean,
        "glycogen": glycogen,
        "bf_pct": bf_pct_arr,
        "tdee": tdee_arr,
    })

    total_lean_change = lean[-1] - lean[0]
    weeks = max(1, n_days / 7)
    avg_weekly_muscle_gain_g = (total_lean_change / weeks) * 1000

    meta = {
        "protein_pct": protein_pct,
        "fat_pct": fat_pct_macro,
        "carb_pct": carb_pct_macro,
        "avg_weekly_muscle_gain_g": avg_weekly_muscle_gain_g,
        "initial_bf_pct": bf_pct_initial,
    }

    return df, meta
