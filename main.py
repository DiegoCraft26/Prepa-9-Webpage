import streamlit as st

#Title
st.title("Taller de Informatica y Matematicas")

#Header
st.header("Preparatoria 9")

#add a logo in the left corner
from PIL import Image
image = Image.open('prepa9logo.png')
st.image(image, width=100)
