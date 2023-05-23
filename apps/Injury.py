import streamlit as st
from streamlit_option_menu import option_menu
from rules.injury_tab_rules import CommonInjury, InjuryType, PreventionType, Prevention

def app():
    # Sidebar
    with st.sidebar:
        selected = option_menu(
            menu_title=None,
            options=["Common Injury", "Treatment", "Prevention"],
            default_index=0,
            icons=["heart-pulse-fill", "capsule", "shield-shaded"]
        )

    if selected == "Common Injury":
        st.markdown("""<h1 style="text-align: center;">Common Injury</h1>""", unsafe_allow_html=True)
        injury = st.selectbox(" ", ["Sprain", "Strain", "Knee Injury", "Fractures", "Muscle Cramps", "Nose Injuries", "Bruises", "Cuts and Abrasions", "Dental Damage", "Dislocations"])

        # Run the CommonInjury engine
        engine = CommonInjury()
        engine.reset()
        engine.declare(InjuryType(injury_type=injury))
        engine.run()

    elif selected == "Treatment":
        st.markdown("""<h1 style="text-align: center;">Treatment</h1>""", unsafe_allow_html=True)
        injury = st.selectbox(" ", [])

    elif selected == "Prevention":
        st.markdown("""<h1 style="text-align: center;">Prevention</h1>""", unsafe_allow_html=True)
        prevention = st.selectbox(" ", ["Always Warm Up Beforehand", "Exercise Regularly", "Do not Push Your Body Beyond Its Limits", "Use the Proper Technique", "Have the Proper Equipment", "Cool Down", "Resume Activity Slowly"])

        # Run the Prevention engine
        engine = Prevention()
        engine.reset()
        engine.declare(PreventionType(prevention_type=prevention))
        engine.run()