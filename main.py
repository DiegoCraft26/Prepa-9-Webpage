import streamlit as st

# Title
st.title("Taller de Informatica y Matematicas")

# Header
st.header("Preparatoria 9")

# Add logo
with open("style.css", "r") as f:
  style = f.read()

st.markdown("""
<style>
%s
</style>
""" % style, unsafe_allow_html=True)

st.markdown("""
<img src="https://imgur.com/hUoBM5a" style="width: 100px; height: 100px;" />
""", unsafe_allow_html=True)
