import streamlit as st
from pathlib import Path

from src.ui.about import show_about

st.set_page_config(
    page_title="About Project",
    page_icon="ℹ️",
    layout="wide"
)

css_file = Path("assets/style.css")

with open(css_file) as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

show_about()