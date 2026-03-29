"""Plotly chart builders with animations and interactivity."""

from __future__ import annotations

import pandas as pd
import plotly.graph_objects as go

from src.i18n import t

_LAYOUT_DEFAULTS = {
    "template": "plotly_dark",
    "paper_bgcolor": "rgba(0,0,0,0)",
    "plot_bgcolor": "rgba(0,0,0,0)",
    "font": {"family": "Inter, system-ui, sans-serif", "size": 13},
    "margin": {"l": 40, "r": 20, "t": 50, "b": 40},
    "hovermode": "x unified",
    "legend": {"orientation": "h", "yanchor": "bottom", "y": 1.02, "xanchor": "right", "x": 1},
}

_HOVER_KG = "%{x|%b %d}<br>%{y:.1f} kg<extra></extra>"


def _hex_to_rgba(hex_color: str, alpha: float = 0.2) -> str:
    """Convert a hex color string to an rgba() string with the given alpha."""
    hex_color = hex_color.lstrip("#")
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)
    return f"rgba({r},{g},{b},{alpha})"


def plot_weight_evolution(df: pd.DataFrame, color: str, lang: str = "en") -> go.Figure:
    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=df["date"],
            y=df["weight"],
            mode="lines+markers",
            name=t("weight_label", lang),
            line={"color": color, "width": 3},
            marker={"size": 4},
            hovertemplate=_HOVER_KG,
        )
    )

    # 7-day rolling trend
    if len(df) >= 7:
        df_rolling = df.set_index("date")["weight"].rolling(7, min_periods=1).mean()
        fig.add_trace(
            go.Scatter(
                x=df_rolling.index,
                y=df_rolling.values,
                mode="lines",
                name=t("trend_7d", lang),
                line={"color": color, "width": 1.5, "dash": "dash"},
                opacity=0.6,
                hovertemplate=_HOVER_KG,
            )
        )

    fig.update_layout(
        **_LAYOUT_DEFAULTS,
        title=t("weight_over_time", lang),
        yaxis_title=t("weight_kg_axis", lang),
        xaxis_title="",
    )

    return fig


def plot_body_composition(
    df: pd.DataFrame, color_fat: str, color_lean: str, lang: str = "en"
) -> go.Figure:
    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=df["date"],
            y=df["fat"],
            fill="tozeroy",
            name=t("fat_mass_label", lang),
            line={"color": color_fat, "width": 2},
            fillcolor=_hex_to_rgba(color_fat, 0.2),
            hovertemplate=_HOVER_KG,
        )
    )

    fig.add_trace(
        go.Scatter(
            x=df["date"],
            y=df["lean"],
            fill="tozeroy",
            name=t("lean_mass_label", lang),
            line={"color": color_lean, "width": 2},
            fillcolor=_hex_to_rgba(color_lean, 0.2),
            hovertemplate=_HOVER_KG,
        )
    )

    fig.add_trace(
        go.Scatter(
            x=df["date"],
            y=df["glycogen"],
            name=t("glycogen_water", lang),
            line={"color": "#a78bfa", "width": 1.5, "dash": "dot"},
            hovertemplate=_HOVER_KG,
        )
    )

    fig.update_layout(
        **_LAYOUT_DEFAULTS,
        title=t("composition_over_time", lang),
        yaxis_title=t("weight_kg_axis", lang),
        xaxis_title="",
    )

    return fig


def plot_bf_gauge(bf_pct: float, lang: str = "en") -> go.Figure:
    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=bf_pct,
            number={"suffix": "%", "font": {"size": 28}},
            title={"text": t("body_fat_pct", lang), "font": {"size": 14}},
            gauge={
                "axis": {"range": [5, 40], "tickwidth": 1},
                "bar": {"color": "#3b82f6"},
                "steps": [
                    {"range": [5, 10], "color": "#22c55e"},
                    {"range": [10, 18], "color": "#84cc16"},
                    {"range": [18, 25], "color": "#eab308"},
                    {"range": [25, 32], "color": "#f97316"},
                    {"range": [32, 40], "color": "#ef4444"},
                ],
                "threshold": {
                    "line": {"color": "white", "width": 3},
                    "thickness": 0.8,
                    "value": bf_pct,
                },
            },
        )
    )

    fig.update_layout(**_LAYOUT_DEFAULTS, height=250)
    return fig


def plot_muscle_gain_rate(weekly_gain_g: float, lang: str = "en") -> go.Figure:
    fig = go.Figure(
        go.Indicator(
            mode="number+delta",
            value=weekly_gain_g,
            number={"suffix": " g/wk", "font": {"size": 24}},
            title={"text": t("avg_lean_change", lang), "font": {"size": 14}},
            delta={
                "reference": 0,
                "relative": False,
                "valueformat": ".0f",
                "suffix": " g",
                "increasing": {"color": "#22c55e"},
                "decreasing": {"color": "#ef4444"},
            },
        )
    )

    fig.update_layout(**_LAYOUT_DEFAULTS, height=250)
    return fig


def plot_macro_split(
    protein_pct: float, fat_pct: float, carb_pct: float, lang: str = "en"
) -> go.Figure:
    labels = [t("protein", lang), t("fat", lang), t("carbs", lang)]
    values = [max(0, protein_pct), max(0, fat_pct), max(0, carb_pct)]
    colors = ["#3b82f6", "#f97316", "#22c55e"]

    fig = go.Figure(
        go.Pie(
            labels=labels,
            values=values,
            hole=0.55,
            marker={"colors": colors},
            textinfo="label+percent",
            textposition="outside",
            hovertemplate="%{label}: %{percent}<extra></extra>",
        )
    )

    fig.update_layout(
        **_LAYOUT_DEFAULTS,
        title={"text": t("macro_split", lang), "font": {"size": 14}},
        height=250,
        showlegend=False,
    )
    return fig
