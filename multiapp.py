"""Frameworks for running multiple Streamlit applications as a single app.
"""
import streamlit as st
from streamlit_option_menu import option_menu

class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({
            "title": title,
            "function": func
        })

    def run(self):
        st.markdown("""---""")

        # Get the selected option
        selected = option_menu(
            menu_title=None,
            options=[app["title"] for app in self.apps],
            icons=["house-door-fill", "universal-access", "heart-pulse-fill"],
            default_index=0,
            orientation="horizontal"
        )

        st.markdown("""---""")

        # Call the selected function
        for app in self.apps:
            if app["title"] == selected:
                app["function"]()
        