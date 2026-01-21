
st.markdown("""
### Welcome
This platform supports students preparing for the English Language Olympiad (ELO).
""")
import streamlit as st
from sympy import symbols, solve, sympify, latex, expand, factor
import numpy as np
import matplotlib.pyplot as plt
import re

# =====================
# Page config
# =====================
st.set_page_config(
    page_title="Math AI | ELO",
    layout="wide"
)

# =====================
# Header (Logo in all app)
# =====================
col1, col2 = st.columns([1, 5])
with col1:
    st.image("elo_logo.png", width=140)
with col2:
    st.markdown("""
    <h1 style='margin-bottom:0;'>🧮 Math AI</h1>
    <p style='font-size:16px;'>
    Official Training Platform for<br>
    <strong>English Language Olympiad (ELO)</strong>
    </p>
    """, unsafe_allow_html=True)

st.divider()

x = symbols("x")

# =====================
# Helper
# =====================
def convert_math(text):
    text = text.replace(" ", "")
    text = text.replace("^", "**")
    text = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', text)
    return text

# =====================
# Tabs (MAIN IDEA)
# =====================
tab1, tab2, tab3, tab4 = st.tabs([
    "🔢 Math Operations",
    "📐 Equation Solver",
    "📊 Function Plot",
    "🇬🇧 ELO Training"
])

# ---------------------
# Tab 1
# ---------------------
with tab1:
    a = st.number_input("First number", value=0.0)
    b = st.number_input("Second number", value=0.0)

    op = st.selectbox("Operation", ["Add", "Subtract", "Multiply", "Divide"])

    if st.button("Calculate"):
        if op == "Divide" and b == 0:
            st.error("Cannot divide by zero")
        else:
            result = {
                "Add": a + b,
                "Subtract": a - b,
                "Multiply": a * b,
                "Divide": a / b
            }[op]
            st.success(f"Result = {result}")

# ---------------------
# Tab 2
# ---------------------
with tab2:
    eq = st.text_input("Enter equation (example: x^2 - 4x + 3 = 0)")
    if st.button("Solve Equation"):
        try:
            left, right = convert_math(eq).split("=")
            expr = expand(sympify(left) - sympify(right))
            st.latex(f"{latex(expr)} = 0")

            for s in solve(expr, x):
                st.latex(f"x = {latex(s)}")
        except:
            st.error("Invalid equation format")

# ---------------------
# Tab 3
# ---------------------
with tab3:
    func = st.text_input("Enter function (example: x^2 - 4x + 3)")
    if st.button("Plot Function"):
        try:
            f = sympify(convert_math(func))
            xs = np.linspace(-10, 10, 400)
            ys = [f.subs(x, i) for i in xs]

            fig, ax = plt.subplots()
            ax.plot(xs, ys)
            ax.axhline(0)
            ax.axvline(0)
            ax.grid(True)
            st.pyplot(fig)
        except:
            st.error("Invalid function")

# ---------------------
# Tab 4 (ELO)
# ---------------------
with tab4:
    st.subheader("Choose the correct sentence:")

    q = st.radio(
        "",
        [
            "She don't like coffee.",
            "She doesn't like coffee.",
            "She doesn't likes coffee."
        ]
    )

    if st.button("Submit Answer"):
        if q == "She doesn't like coffee.":
            st.success("Correct ✅")
        else:
            st.error("Incorrect ❌")

# =====================
# Footer
# =====================
st.divider()
st.caption("© 2025 Ghada Alotaibi | English Language Olympiad")
