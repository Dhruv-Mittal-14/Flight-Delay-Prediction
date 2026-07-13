import streamlit as st
from pathlib import Path

from src.ui.home import show_home

st.set_page_config(
    page_title="Flight Delay Prediction",
    page_icon="✈",
    layout="wide"
)

css_file = Path("assets/style.css")

with open(css_file) as f:

    st.markdown(

        f"<style>{f.read()}</style>",

        unsafe_allow_html=True

    )

show_home()