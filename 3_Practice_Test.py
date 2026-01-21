import streamlit as st
import time
from utils.header import show_header

st.set_page_config(layout="wide")
show_header()

st.header("📝 Practice Test")

if "start" not in st.session_state:
    st.session_state.start = None

if st.button("Start Test"):
    st.session_state.start = time.time()

if st.session_state.start:
    elapsed = int(time.time() - st.session_state.start)
    st.info(f"Time elapsed: {elapsed} seconds")
