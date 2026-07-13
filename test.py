import streamlit as st

st.title("Test")

page = st.sidebar.radio(
    "Navigation",
    ["Home", "Dashboard", "About"],
    index=0
)

st.write("repr(page):", repr(page))
st.write("type(page):", type(page))
st.write("page == 'Home':", page == "Home")