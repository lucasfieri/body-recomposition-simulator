"""
Optional HuggingFace body fat estimation using ChanMeng666/bodyfat-estimation-mlp.
"""

from __future__ import annotations

import numpy as np
import streamlit as st

from src.i18n import t

try:
    from huggingface_hub import hf_hub_download

    HF_AVAILABLE = True
    HF_IMPORT_ERROR = ""
except ImportError as e:
    HF_AVAILABLE = False
    HF_IMPORT_ERROR = str(e)

_MODEL_REPO = "ChanMeng666/bodyfat-estimation-mlp"
_MODEL_FILE = "best_selected_features_model.keras"


@st.cache_resource
def _load_model():
    """Download and load the HuggingFace body fat MLP model."""
    try:
        import tensorflow as tf

        model_path = hf_hub_download(repo_id=_MODEL_REPO, filename=_MODEL_FILE)
        model = tf.keras.models.load_model(model_path)
        return model, None
    except ImportError as e:
        return None, f"tensorflow_missing: {e}"
    except Exception as e:
        return None, str(e)


def render_hf_bodyfat_panel(
    lang: str = "en", weight_kg: float = 78.0, height_cm: float = 176.0
) -> float | None:
    """
    Render the HuggingFace body fat estimation panel.
    Returns estimated BF% or None if not used / not available.
    Accepts metric values from sidebar and auto-converts to imperial for the model.
    """
    if not HF_AVAILABLE:
        st.error(t("hf_missing_dependency", lang).format(package="huggingface-hub"))
        st.code("uv add huggingface-hub", language="bash")
        if HF_IMPORT_ERROR:
            st.caption(t("hf_tech_details", lang).format(error=HF_IMPORT_ERROR))
        return None

    st.markdown(t("hf_description", lang))

    if "hf_bf_estimate" not in st.session_state:
        st.session_state["hf_bf_estimate"] = None

    use_hf = st.checkbox(t("hf_use_ai", lang), value=False, key="hf_enable")

    if not use_hf:
        return None

    # Auto-convert from metric sidebar values
    default_weight_lbs = round(weight_kg * 2.20462, 1)
    default_height_in = round(height_cm / 2.54, 1)

    st.caption(t("hf_auto_convert", lang))

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.number_input(t("age", lang), 18, 80, 28, key="hf_age")
        weight_lbs = st.number_input(
            t("hf_weight_lbs", lang), 100.0, 400.0, default_weight_lbs, key="hf_weight"
        )
        height_in = st.number_input(
            t("hf_height_in", lang), 50.0, 85.0, default_height_in, key="hf_height"
        )

    with col2:
        neck = st.number_input(t("hf_neck", lang), 25.0, 55.0, 38.0, key="hf_neck_input")
        chest = st.number_input(t("hf_chest", lang), 70.0, 140.0, 100.0, key="hf_chest_input")
        abdomen = st.number_input(t("hf_abdomen", lang), 60.0, 150.0, 85.0, key="hf_abdomen_input")

    with col3:
        hip = st.number_input(t("hf_hip", lang), 70.0, 150.0, 98.0, key="hf_hip_input")
        thigh = st.number_input(t("hf_thigh", lang), 40.0, 85.0, 59.0, key="hf_thigh_input")
        wrist = st.number_input(t("hf_wrist", lang), 13.0, 22.0, 17.0, key="hf_wrist_input")

    if st.button(t("hf_estimate_btn", lang), key="hf_estimate"):
        with st.spinner(t("hf_loading", lang)):
            model, load_error = _load_model()

        if model is None:
            if load_error and load_error.startswith("tensorflow_missing"):
                st.error(t("hf_missing_dependency", lang).format(package="tensorflow"))
                st.code("uv add tensorflow", language="bash")
            else:
                st.error(t("hf_error", lang))

            if load_error:
                st.caption(t("hf_tech_details", lang).format(error=load_error))
            return None

        features = np.array([
            [age, weight_lbs, height_in, neck, chest, abdomen, hip, thigh, wrist]
        ])

        try:
            prediction = model.predict(features, verbose=0)
            bf_pct = float(prediction[0][0])
            bf_pct = max(3.0, min(50.0, bf_pct))
            st.session_state["hf_bf_estimate"] = bf_pct

            st.success(f"**{t('hf_result', lang)}: {bf_pct:.1f}%**")
            st.caption(t("hf_result_caption", lang))
            return bf_pct
        except Exception as e:
            st.error(t("hf_prediction_failed_friendly", lang))
            st.caption(t("hf_tech_details", lang).format(error=str(e)))
            return None

    stored_bf = st.session_state.get("hf_bf_estimate")
    if stored_bf is not None:
        st.info(f"{t('hf_current_result', lang)}: {stored_bf:.1f}%")
    return stored_bf
