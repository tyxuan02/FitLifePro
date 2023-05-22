import streamlit as st
from streamlit_option_menu import option_menu

def app():

    with st.sidebar:
        selected = option_menu(
            menu_title=None,
            options=["Common Injury", "Treatment", "Prevention"],
            default_index=0,
            icons=["heart-pulse-fill", "capsule", "shield-shaded"]
        )

    if selected == "Common Injury":
        st.write("Common Injury")
    elif selected == "Treatment":
        st.write("Treatment")
    elif selected == "Prevention":
        st.write("Prevention")