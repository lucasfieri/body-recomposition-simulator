"""Streamlit UI components for sidebar and scenario panels."""

from __future__ import annotations

from datetime import date, timedelta

import streamlit as st

from src.i18n import t
from src.model import TrainingLevel


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
    sleep = st.sidebar.slider(t("sleep_hours", lang), 4.0, 10.0, 6.5, step=0.5)

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
    }


def render_scenario_panel(
    name: str,
    default_protein: float,
    default_fat_pct: int,
    default_calorie_delta: int,
    lang: str,
) -> dict:
    """Render configuration sliders for a single scenario."""
    st.markdown(f"### {name} — {t('configuration', lang)}")

    protein = st.slider(
        t("protein_g_kg", lang),
        1.2,
        3.0,
        default_protein,
        step=0.1,
        key=f"{name}_protein",
        help=t("protein_help", lang),
    )
    fat_pct = st.slider(
        t("fat_pct_cal", lang),
        15,
        45,
        default_fat_pct,
        key=f"{name}_fat",
        help=t("fat_help", lang),
    )
    calorie_delta = st.slider(
        t("calorie_delta", lang),
        -1000,
        1000,
        default_calorie_delta,
        step=50,
        key=f"{name}_cal",
        help=t("calorie_delta_help", lang),
    )

    carb_cycling = st.checkbox(
        t("carb_cycling", lang),
        key=f"{name}_carb_cycle",
    )
    high_days = 2
    carb_increase = 20.0
    if carb_cycling:
        high_days = st.slider(
            t("high_carb_days", lang),
            1,
            5,
            2,
            key=f"{name}_high_days",
        )
        carb_increase = st.slider(
            t("carb_increase", lang),
            5.0,
            40.0,
            20.0,
            step=5.0,
            key=f"{name}_carb_inc",
        )

    return {
        "protein": protein,
        "fat_pct": fat_pct,
        "calorie_delta": calorie_delta,
        "carb_cycling": carb_cycling,
        "high_days": high_days,
        "carb_increase": carb_increase,
    }
