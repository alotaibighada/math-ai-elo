import streamlit as st

def show_header():
    col1, col2 = st.columns([1, 4])
    with col1:
        st.image("elo_logo.png", width=150)
    with col2:
        st.markdown("""
        <h1 style='color:#1E3C72;margin-bottom:0;'>🧮 Math AI</h1>
        <p style='color:#444;font-size:15px;'>
            Official Training Platform for<br>
            <strong>English Language Olympiad (ELO)</strong>
        </p>
        """, unsafe_allow_html=True)
    st.markdown("---")
