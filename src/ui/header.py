import streamlit as st


def show_header():

    st.markdown(
        """
        <div class="main-title">

            ✈ Flight Delay Prediction System

        </div>

        <div class="sub-title">

            AI Powered Flight Analytics Platform

        </div>

        """,
        unsafe_allow_html=True
    )