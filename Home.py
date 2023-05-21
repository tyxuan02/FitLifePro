import streamlit as st
from streamlit_option_menu import option_menu

selected = option_menu(
    menu_title="Main Menu",
    options=["Home", "Sports", "Injury"],
    default_index=0,
    orientation="horizontal",
)

st.title("FitLifePro Expert System")


