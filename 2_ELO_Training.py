import streamlit as st
from utils.header import show_header

st.set_page_config(layout="wide")
show_header()

st.header("🇬🇧 English Language Olympiad Training")

choice = st.radio(
    "Choose the correct sentence:",
    [
        "She don't like coffee.",
        "She doesn't like coffee.",
        "She doesn't likes coffee."
    ]
)

if st.button("Submit Answer"):
    if choice == "She doesn't like coffee.":
        st.success("Correct ✅")
    else:
        st.error("Incorrect ❌")
