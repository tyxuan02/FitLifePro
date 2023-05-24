import streamlit as st
from streamlit_option_menu import option_menu
from rules.sports_tab_rules import TeamSportsType, TeamSports 

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
        