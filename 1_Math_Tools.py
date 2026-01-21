import streamlit as st
from sympy import symbols, solve, sympify, latex, expand, lambdify
import numpy as np
import matplotlib.pyplot as plt
import re
from utils.header import show_header

st.set_page_config(layout="wide")
show_header()

x = symbols("x")

def convert_math(text):
    text = text.replace(" ", "").replace("^", "**")
    text = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', text)
    return text

st.header("📐 Math Tools")

a = st.number_input("First Number", value=0.0)
b = st.number_input("Second Number", value=0.0)

if st.button("Add"):
    st.success(a + b)

eq = st.text_input("Equation: x^2 - 4x + 3 = 0")
if st.button("Solve Equation"):
    left, right = convert_math(eq).split("=")
    expr = expand(sympify(left) - sympify(right))
    st.latex(f"{latex(expr)} = 0")
    for s in solve(expr, x):
        st.latex(f"x = {latex(s)}")

func = st.text_input("Function: x^2 - 4x + 3")
if st.button("Plot Function"):
    f = sympify(convert_math(func))
    f_num = lambdify(x, f, "numpy")
    xs = np.linspace(-10, 10, 400)
    ys = f_num(xs)
    fig, ax = plt.subplots()
    ax.plot(xs, ys)
    ax.grid(True)
    st.pyplot(fig)
