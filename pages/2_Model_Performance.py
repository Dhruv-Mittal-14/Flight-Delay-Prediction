import streamlit as st
from pathlib import Path

from src.ui.model_performance import show_model_performance

st.set_page_config(
    page_title="Model Performance",
    page_icon="🤖",
    layout="wide"
)

css_file = Path("assets/style.css")

with open(css_file) as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

show_model_performance()