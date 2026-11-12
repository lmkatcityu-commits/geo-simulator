import streamlit as st

st.set_page_config(page_title="IS4340 GEO Simulator", layout="wide")
st.title("IS4340 GEO Simulation Platform (Revlon Case Study)")
st.write("Welcome! Paste your rewritten Task 2 product copy below to test AI visibility.")

student_copy = st.text_area("Rewritten Revlon Product Copy & JSON-LD Schema:", height=150)
query = st.text_input("Target Test Query:", value="best color stay lipstick")

if st.button("Run Simulation"):
    st.success(f"Testing query: '{query}' — Simulation engine connected!")
