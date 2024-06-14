import streamlit as st
from predict_page import show_predict_page


with open("style.css") as source_design:
    st.markdown(f"<style>{source_design.read()} </style>", unsafe_allow_html=True)

show_predict_page()
