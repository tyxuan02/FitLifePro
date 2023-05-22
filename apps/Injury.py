import streamlit as st
from streamlit_option_menu import option_menu
from experta import Rule, Fact, KnowledgeEngine

class InjuryType(Fact):
    """Info about the injury type"""
    pass

class CommonInjury(KnowledgeEngine):
    @Rule(InjuryType(injury_type='Sprain'))
    def sprain(self):
        st.write("Sprain")

    @Rule(InjuryType(injury_type='Strain'))
    def strain(self):
        st.write("Strain")


def app():
    with st.sidebar:
        selected = option_menu(
            menu_title=None,
            options=["Common Injury", "Treatment", "Prevention"],
            default_index=0,
            icons=["heart-pulse-fill", "capsule", "shield-shaded"]
        )

    if selected == "Common Injury":
        st.markdown("""<h2 style="text-align: center;">Common Injury</h2>""", unsafe_allow_html=True)

        st.markdown("""<h4>Select the type of injury</h4>""", unsafe_allow_html=True)
        injury = st.selectbox("", ["Sprain", "Strain"])

        engine = CommonInjury()
        engine.reset()
        engine.declare(InjuryType(injury_type=injury))
        engine.run()

    elif selected == "Treatment":
        st.write("Treatment")
    elif selected == "Prevention":
        st.write("Prevention")