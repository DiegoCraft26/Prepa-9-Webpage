import streamlit as st

# Importing the pages
from pages import home, data, model, about

#Title
st.title("Taller de Informatica y Matematicas")
# Subheader
st.subheader("Preparatoria 9")

# Creating the Navigation Bar
menu = ["Home", "Informatica", "Matematicas", "About"]

choice = st.sidebar.selectbox("Menu", menu)

if choice == "Home":
    home.app()
elif choice == "Informatica":
    data.app()
elif choice == "Matematicas":
    model.app()
else:
    about.app()

# Footer
st.sidebar.markdown(
    """
    [Github]("https://github.com/DiegoCraft26/Prepa-9-Webpage")
    """
)


