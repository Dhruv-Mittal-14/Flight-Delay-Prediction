import streamlit as st


def show_footer():

    st.markdown(
        """
        <hr>

        <div class="footer">

        Developed by <b>Dhruv Mittal</b><br>

        MCA (Data Science)<br>

        Flight Delay Prediction System ©2026

        </div>
        """,
        unsafe_allow_html=True
    )