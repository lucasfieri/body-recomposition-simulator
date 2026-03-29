"""
Body Recomposition Simulator
Main Streamlit application entry point.
"""

import streamlit as st

from src.charts import (
    plot_bf_gauge,
    plot_body_composition,
    plot_macro_split,
    plot_muscle_gain_rate,
    plot_weight_evolution,
)
from src.hf_bodyfat import render_hf_bodyfat_panel
from src.i18n import t
from src.model import SimulationParams, simulate
from src.references import render_references
from src.ui import render_scenario_panel, render_sidebar

st.set_page_config(
    layout="wide",
    page_title="Body Recomp Simulator",
    page_icon="💪",
)

st.markdown(
    """
    <style>
    .block-container { padding-top: 1.5rem; }
    .stTabs [data-baseweb="tab-list"] { gap: 2rem; }
    .stTabs [data-baseweb="tab"] {
        font-size: 1.05rem;
        font-weight: 600;
    }
    .bf-status-badge {
        position: fixed;
        top: 0.75rem;
        right: 1rem;
        z-index: 1000;
        padding: 0.45rem 0.8rem;
        border-radius: 999px;
        font-size: 0.82rem;
        font-weight: 700;
        box-shadow: 0 6px 16px rgba(0, 0, 0, 0.25);
        border: 1px solid rgba(255, 255, 255, 0.2);
    }
    .bf-status-active {
        background: rgba(34, 197, 94, 0.18);
        color: #bbf7d0;
    }
    .bf-status-inactive {
        background: rgba(251, 191, 36, 0.16);
        color: #fde68a;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ── Language selector (top of sidebar) ────────────────���──────────────────────
_browser_locale = getattr(st.context, "locale", "en") or "en"
_default_lang_index = 1 if _browser_locale.startswith("pt") else 0

lang = st.sidebar.selectbox(
    t("language", lang="en") + " / " + t("language", lang="pt"),
    ["en", "pt"],
    index=_default_lang_index,
    format_func=lambda x: "English" if x == "en" else "Português",
)

st.title(t("app_title", lang))
st.caption(t("app_caption", lang))

# ── Sidebar ──────────────────────────────────────────────────────────────────
sidebar_params = render_sidebar(lang)

# ── HuggingFace body fat estimation (optional) ──────────────────────────────
with st.expander(t("hf_title", lang), expanded=False):
    hf_bf = render_hf_bodyfat_panel(lang, sidebar_params["weight"], sidebar_params["height"])

initial_bf = hf_bf if hf_bf is not None else None
using_ai_bf = st.session_state.get("hf_enable", False) and initial_bf is not None

status_class = "bf-status-active" if using_ai_bf else "bf-status-inactive"
status_text = (
    t("bf_badge_active", lang).format(bf=initial_bf)
    if using_ai_bf
    else t("bf_badge_inactive", lang)
)
st.markdown(
    f'<div class="bf-status-badge {status_class}">{status_text}</div>',
    unsafe_allow_html=True,
)

# ── Scenario Tabs ────────────────────────────────────────────────────────────
tab_cut, tab_recomp, tab_bulk = st.tabs([
    t("tab_cut", lang),
    t("tab_recomp", lang),
    t("tab_bulk", lang),
])


def run_scenario(
    tab,
    scenario_key: str,
    scenario_name: str,
    default_protein: float,
    default_fat_pct: int,
    default_calories_delta: int,
    color_primary: str,
    color_secondary: str,
):
    """Render a full scenario inside its tab."""
    with tab:
        col_config, col_charts = st.columns([1, 3], gap="medium")

        with col_config:
            params = render_scenario_panel(
                scenario_key,
                scenario_name,
                default_protein,
                default_fat_pct,
                default_calories_delta,
                lang,
                initial_bf,
                sidebar_params["training_level"],
            )

        sim_params = SimulationParams(
            age=sidebar_params["age"],
            height_cm=sidebar_params["height"],
            initial_weight_kg=sidebar_params["weight"],
            sleep_hours=sidebar_params["sleep"],
            protein_g_per_kg=params["protein"],
            fat_pct=params["fat_pct"],
            calorie_delta=params["calorie_delta"],
            carb_cycling=params["carb_cycling"],
            carb_cycling_high_days=params["high_days"],
            carb_cycling_increase_pct=params["carb_increase"],
            training_level=sidebar_params["training_level"],
            training_days_per_week=sidebar_params["training_days"],
            start_date=sidebar_params["start"],
            end_date=sidebar_params["end"],
            neat_steps_per_day=sidebar_params["neat_steps"],
            alcohol_drinks_per_week=sidebar_params["alcohol_drinks_week"],
            adherence_pct=sidebar_params["adherence_pct"],
            initial_bf_pct=initial_bf,
            sex=sidebar_params["sex"],
        )

        df, meta = simulate(sim_params)

        # Apply view frequency
        freq = sidebar_params["freq"]
        gran = sidebar_params["granularity"]
        step = max(1, freq)
        if gran == "Weeks":
            step *= 7
        elif gran == "Months":
            step *= 30
        df_view = df.iloc[::step].copy()

        with col_charts:
            st.subheader(f"{scenario_name} — {t('projected_results', lang)}")

            if using_ai_bf:
                st.warning(t("hf_chart_applied_notice", lang).format(bf=initial_bf))

            metric_cols = st.columns(4)
            final = df.iloc[-1]
            initial = df.iloc[0]
            metric_cols[0].metric(
                t("final_weight", lang),
                f"{final['weight']:.1f} kg",
                f"{final['weight'] - initial['weight']:.1f} kg",
            )
            metric_cols[1].metric(
                t("final_bf", lang),
                f"{final['bf_pct']:.1f}%",
                f"{final['bf_pct'] - initial['bf_pct']:.1f}%",
                delta_color="inverse",
            )
            metric_cols[2].metric(
                t("lean_mass", lang),
                f"{final['lean']:.1f} kg",
                f"{final['lean'] - initial['lean']:.1f} kg",
            )
            metric_cols[3].metric(
                t("fat_mass", lang),
                f"{final['fat']:.1f} kg",
                f"{final['fat'] - initial['fat']:.1f} kg",
                delta_color="inverse",
            )

            st.divider()

            chart_tab1, chart_tab2, chart_tab3 = st.tabs([
                t("chart_weight", lang),
                t("chart_composition", lang),
                t("chart_metrics", lang),
            ])

            with chart_tab1:
                st.plotly_chart(
                    plot_weight_evolution(df_view, color_primary, lang),
                    width="stretch",
                    key=f"{scenario_key}_chart_weight",
                )

            with chart_tab2:
                st.plotly_chart(
                    plot_body_composition(df_view, color_primary, color_secondary, lang),
                    width="stretch",
                    key=f"{scenario_key}_chart_composition",
                )

            with chart_tab3:
                g1, g2, g3 = st.columns(3)
                with g1:
                    st.plotly_chart(
                        plot_bf_gauge(final["bf_pct"], lang),
                        width="stretch",
                        key=f"{scenario_key}_chart_bf_gauge",
                    )
                with g2:
                    st.plotly_chart(
                        plot_muscle_gain_rate(meta["avg_weekly_muscle_gain_g"], lang),
                        width="stretch",
                        key=f"{scenario_key}_chart_muscle_rate",
                    )
                with g3:
                    st.plotly_chart(
                        plot_macro_split(
                            meta["protein_pct"],
                            meta["fat_pct"],
                            meta["carb_pct"],
                            lang,
                        ),
                        width="stretch",
                        key=f"{scenario_key}_chart_macro_split",
                    )


# ── Render each scenario ─────────────────────────────────────────────────────
run_scenario(tab_cut, "cut", t("scenario_cut", lang), 2.2, 25, -500, "#ef4444", "#fca5a5")
run_scenario(
    tab_recomp,
    "recomp",
    t("scenario_recomp", lang),
    2.0,
    28,
    0,
    "#3b82f6",
    "#93c5fd",
)
run_scenario(
    tab_bulk,
    "bulk",
    t("scenario_bulk", lang),
    1.8,
    30,
    300,
    "#22c55e",
    "#86efac",
)

# ── Scientific References Footer ─────────────────────────────────────────────
render_references(lang)
