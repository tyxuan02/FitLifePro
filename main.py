import streamlit as st
from multiapp import MultiApp
from apps import Home, Injury, Sports # import your app modules here

st.set_page_config(page_title="FitLifePro", page_icon="💖", layout="wide")


st.markdown(
    """
    <h1 style="text-align: center; font-size: 60px;">FitLifePro</h1>
    """,
    unsafe_allow_html=True
)

app = MultiApp()

# Add all your application here
app.add_app("Home", Home.app)
app.add_app("Sports", Sports.app)
app.add_app("Injury", Injury.app)
# The main app
app.run() 