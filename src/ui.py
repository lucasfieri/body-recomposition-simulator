"""Streamlit UI components for sidebar and scenario panels."""

from __future__ import annotations

from datetime import date, timedelta

import streamlit as st

from src.i18n import t
from src.model import TrainingLevel


def _get_profile_presets() -> dict[str, dict[str, float | int]]:
    """Return built-in nutrition presets by profile."""
    return {
        "beginner": {"protein": 1.8, "fat_pct": 30, "calorie_delta": 0},
        "athlete": {"protein": 2.2, "fat_pct": 25, "calorie_delta": 200},
        "aggressive_cut": {"protein": 2.4, "fat_pct": 22, "calorie_delta": -650},
        "light_recomp": {"protein": 2.0, "fat_pct": 28, "calorie_delta": -100},
    }


def _goal_recommendation(
    current_bf_pct: float | None,
    target_bf_pct: float,
    training_level: TrainingLevel,
) -> dict[str, float | int | str]:
    """Compute automatic macro and calorie recommendations for a target BF goal."""
    current_bf = current_bf_pct if current_bf_pct is not None else 22.0
    bf_gap = target_bf_pct - current_bf

    if bf_gap <= -1.0:
        strategy = "cut"
        calorie_delta = int(max(-900, min(-200, -250 - 40 * abs(bf_gap))))
        fat_pct = 22
        protein = 2.4
    elif bf_gap >= 1.0:
        strategy = "gain"
        calorie_delta = int(max(100, min(350, 120 + 25 * abs(bf_gap))))
        fat_pct = 28
        protein = 1.8
    else:
        strategy = "maintain"
        calorie_delta = 0
        fat_pct = 27
        protein = 2.0

    if training_level == TrainingLevel.ADVANCED:
        if calorie_delta > 0:
            calorie_delta = int(calorie_delta * 0.85)
        else:
            calorie_delta = int(calorie_delta * 0.9)
        protein = max(protein, 2.2)
    elif training_level == TrainingLevel.BEGINNER and calorie_delta < 0:
        calorie_delta = int(calorie_delta * 0.85)

    return {
        "protein": round(min(3.0, max(1.6, protein)), 1),
        "fat_pct": int(min(40, max(18, fat_pct))),
        "calorie_delta": int(min(1000, max(-1000, calorie_delta))),
        "strategy": strategy,
    }


def render_sidebar(lang: str) -> dict:
    """Render the sidebar configuration and return parameters dict."""
    st.sidebar.title(t("settings", lang))

    st.sidebar.header(t("personal_info", lang))
    sex_options = [t("male", lang), t("female", lang)]
    sex_display = st.sidebar.radio(t("sex", lang), sex_options, horizontal=True)
    sex = "Male" if sex_display == sex_options[0] else "Female"

    weight = st.sidebar.slider(t("weight_kg", lang), 45.0, 150.0, 78.0, step=0.5)
    height = st.sidebar.slider(t("height_cm", lang), 140, 210, 176)
    age = st.sidebar.slider(t("age", lang), 16, 70, 28)
    sleep = st.sidebar.slider(
        t("sleep_hours", lang),
        4.0,
        10.0,
        6.5,
        step=0.5,
        help=t("sleep_help", lang),
    )

    st.sidebar.header(t("training", lang))
    level_labels = [t("beginner", lang), t("intermediate", lang), t("advanced", lang)]
    level_enums = [TrainingLevel.BEGINNER, TrainingLevel.INTERMEDIATE, TrainingLevel.ADVANCED]
    level_display = st.sidebar.selectbox(t("training_experience", lang), level_labels, index=1)
    training_level_enum = level_enums[level_labels.index(level_display)]

    training_days = st.sidebar.slider(t("training_days_week", lang), 0, 7, 4)

    st.sidebar.header(t("time_range", lang))
    start = st.sidebar.date_input(t("start", lang), date.today())

    preset_labels = {
        t("custom", lang): 0,
        "30 " + t("days", lang).lower(): 30,
        "60 " + t("days", lang).lower(): 60,
        "90 " + t("days", lang).lower(): 90,
        "180 " + t("days", lang).lower(): 180,
        "365 " + t("days", lang).lower(): 365,
    }
    preset = st.sidebar.selectbox(t("duration_preset", lang), list(preset_labels.keys()), index=3)

    if preset_labels[preset] == 0:
        end = st.sidebar.date_input(t("end", lang), date.today() + timedelta(days=90))
    else:
        end = start + timedelta(days=preset_labels[preset])

    st.sidebar.header(t("view", lang))
    gran_options = [t("days", lang), t("weeks", lang), t("months", lang)]
    granularity = st.sidebar.selectbox(t("granularity", lang), gran_options)
    freq = st.sidebar.slider(t("step", lang), 1, 10, 1)

    st.sidebar.header(t("optional_factors", lang))
    use_optional_factors = st.sidebar.checkbox(
        t("enable_optional_factors", lang),
        value=False,
        help=t("optional_factors_help", lang),
    )

    neat_steps = None
    alcohol_drinks = 0
    adherence_pct = 100
    if use_optional_factors:
        neat_steps = st.sidebar.slider(
            t("neat_steps", lang),
            2000,
            20000,
            7000,
            step=250,
            help=t("neat_steps_help", lang),
        )
        alcohol_drinks = st.sidebar.slider(
            t("alcohol_drinks_week", lang),
            0,
            21,
            0,
            step=1,
            help=t("alcohol_drinks_help", lang),
        )
        adherence_pct = st.sidebar.slider(
            t("adherence_pct", lang),
            60,
            100,
            85,
            step=1,
            help=t("adherence_help", lang),
        )

    # Map display granularity back to internal key
    gran_map = {gran_options[0]: "Days", gran_options[1]: "Weeks", gran_options[2]: "Months"}

    return {
        "sex": sex,
        "weight": weight,
        "height": height,
        "age": age,
        "sleep": sleep,
        "training_level": training_level_enum,
        "training_days": training_days,
        "start": start,
        "end": end,
        "granularity": gran_map[granularity],
        "freq": freq,
        "neat_steps": neat_steps,
        "alcohol_drinks_week": alcohol_drinks,
        "adherence_pct": adherence_pct,
    }


def render_scenario_panel(
    scenario_key: str,
    scenario_label: str,
    default_protein: float,
    default_fat_pct: int,
    default_calorie_delta: int,
    lang: str,
    current_bf_pct: float | None,
    training_level: TrainingLevel,
) -> dict:
    """Render configuration sliders for a single scenario."""
    st.markdown(f"### {scenario_label} - {t('configuration', lang)}")

    protein_key = f"{scenario_key}_protein"
    fat_key = f"{scenario_key}_fat"
    cal_key = f"{scenario_key}_cal"

    if protein_key not in st.session_state:
        st.session_state[protein_key] = default_protein
    if fat_key not in st.session_state:
        st.session_state[fat_key] = default_fat_pct
    if cal_key not in st.session_state:
        st.session_state[cal_key] = default_calorie_delta

    goal_mode = st.checkbox(
        t("goal_mode", lang),
        key=f"{scenario_key}_goal_mode",
        help=t("goal_mode_help", lang),
    )

    preset_label_map = {
        t("profile_beginner", lang): "beginner",
        t("profile_athlete", lang): "athlete",
        t("profile_aggressive_cut", lang): "aggressive_cut",
        t("profile_light_recomp", lang): "light_recomp",
    }
    preset_display = st.selectbox(
        t("profile_preset", lang),
        list(preset_label_map.keys()),
        index=0,
        key=f"{scenario_key}_profile_preset",
        help=t("profile_preset_help", lang),
        disabled=goal_mode,
    )
    if st.button(
        t("apply_profile_preset", lang),
        key=f"{scenario_key}_apply_preset",
        disabled=goal_mode,
    ):
        preset_values = _get_profile_presets()[preset_label_map[preset_display]]
        st.session_state[protein_key] = preset_values["protein"]
        st.session_state[fat_key] = preset_values["fat_pct"]
        st.session_state[cal_key] = preset_values["calorie_delta"]
        st.success(t("profile_preset_applied", lang))
        st.rerun()

    if goal_mode:
        st.caption(t("profile_preset_disabled_in_goal", lang))

    if goal_mode:
        target_bf_pct = st.slider(
            t("goal_target_bf", lang),
            6.0,
            35.0,
            15.0,
            step=0.5,
            key=f"{scenario_key}_target_bf",
        )
        recommendation = _goal_recommendation(current_bf_pct, target_bf_pct, training_level)
        protein = float(recommendation["protein"])
        fat_pct = int(recommendation["fat_pct"])
        calorie_delta = int(recommendation["calorie_delta"])
        current_bf_display = current_bf_pct if current_bf_pct is not None else 22.0
        strategy_label = t(f"goal_strategy_{recommendation['strategy']}", lang)

        st.info(
            t("goal_mode_summary", lang).format(
                current=current_bf_display,
                target=target_bf_pct,
            )
        )
        st.markdown(
            "\n".join([
                f"- **{t('goal_item_strategy', lang)}:** {strategy_label}",
                (
                    f"- **{t('goal_item_calorie_delta', lang)}:** "
                    f"{calorie_delta:+.0f} kcal/{t('days', lang).lower()}"
                ),
                f"- **{t('goal_item_protein', lang)}:** {protein:.1f} g/kg",
                f"- **{t('goal_item_fat', lang)}:** {fat_pct}%",
            ])
        )
        st.caption(t("goal_mode_reference", lang))
    else:
        protein = st.slider(
            t("protein_g_kg", lang),
            1.2,
            3.0,
            step=0.1,
            key=protein_key,
            help=t("protein_help", lang),
        )
        fat_pct = st.slider(
            t("fat_pct_cal", lang),
            15,
            45,
            key=fat_key,
            help=t("fat_help", lang),
        )
        calorie_delta = st.slider(
            t("calorie_delta", lang),
            -1000,
            1000,
            step=50,
            key=cal_key,
            help=t("calorie_delta_help", lang),
        )

    carb_cycling = st.checkbox(
        t("carb_cycling", lang),
        key=f"{scenario_key}_carb_cycle",
        help=t("carb_cycling_help", lang),
    )
    high_days = 2
    carb_increase = 20.0
    if carb_cycling:
        high_days = st.slider(
            t("high_carb_days", lang),
            1,
            5,
            2,
            key=f"{scenario_key}_high_days",
            help=t("high_carb_days_help", lang),
        )
        carb_increase = st.slider(
            t("carb_increase", lang),
            5.0,
            40.0,
            20.0,
            step=5.0,
            key=f"{scenario_key}_carb_inc",
            help=t("carb_increase_help", lang),
        )

    return {
        "protein": protein,
        "fat_pct": fat_pct,
        "calorie_delta": calorie_delta,
        "carb_cycling": carb_cycling,
        "high_days": high_days,
        "carb_increase": carb_increase,
    }
