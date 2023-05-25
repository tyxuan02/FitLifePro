import streamlit as st
from streamlit_option_menu import option_menu
from rules.sports_tab_rules import TeamSportsType, TeamSports, IndividualSportsType, IndividualSports

def app():

    # Insert Sports Tab code here
    with st.sidebar:
        selected = option_menu(
            menu_title=None,
            options=["Team Sports", "Individual Sports"],
            default_index=0,
            icons=["people-fill", "person-fill"]
        )
        
    if selected == "Team Sports":
        st.markdown("""<h1 style="text-align: center;">Team Sports</h1>""", unsafe_allow_html=True)
        Sports = st.selectbox(" ", ["Football", "Basketball", "Rugby", "Hockey", "Baseball", "Volleyball", "Handball"])
        
        # Run the Team Sports engine
        engine = TeamSports()
        engine.reset()
        engine.declare(TeamSportsType(teamSports_type=Sports))
        engine.run()

    if selected == "Individual Sports":
        st.markdown("""<h1 style="text-align: center;">Individual Sports</h1>""", unsafe_allow_html=True)
        Sports = st.selectbox(" ", ["Swimming","Workout","Cycling"])
        
        # Run the Team Sports engine
        engine = IndividualSports()
        engine.reset()
        engine.declare(IndividualSportsType(individualSports_type=Sports))
        engine.run()
        