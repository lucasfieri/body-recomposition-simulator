"""Render the scientific references accordion in the footer."""

from __future__ import annotations

import streamlit as st

from src.i18n import t

_REFERENCE_KEYS = [
    ("ref_mifflin_title", "ref_mifflin_desc"),
    ("ref_katch_title", "ref_katch_desc"),
    ("ref_thermogenesis_title", "ref_thermogenesis_desc"),
    ("ref_aragon_title", "ref_aragon_desc"),
    ("ref_pratio_title", "ref_pratio_desc"),
    ("ref_tef_title", "ref_tef_desc"),
    ("ref_deurenberg_title", "ref_deurenberg_desc"),
    ("ref_issn_title", "ref_issn_desc"),
    ("ref_neat_title", "ref_neat_desc"),
    ("ref_alcohol_title", "ref_alcohol_desc"),
    ("ref_adherence_title", "ref_adherence_desc"),
    ("ref_hf_title", "ref_hf_desc"),
]


def render_references(lang: str = "en") -> None:
    """Render the scientific evidence accordion at the bottom of the page."""
    st.divider()
    st.header(t("references_title", lang))

    for title_key, desc_key in _REFERENCE_KEYS:
        with st.expander(t(title_key, lang)):
            st.markdown(t(desc_key, lang))
