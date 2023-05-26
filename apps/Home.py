import streamlit as st
from rules.home_tab_rules import Gender, Age, Weight, Height, Lifestyle, CalculateIntake, BMITableEngine, BMITable, HealthTips, HealthTipsEngine

def app():
    # Insert Home Tab code here

    with st.sidebar:
        st.title("Let's get started!")
        name = st.text_input("How would you like us to address you?")
        age = st.slider("How old are you?", 10, 60, 18, 1)
        gender = st.selectbox("What is your gender?", ["Male", "Female"])
        height = st.slider("What is your height (cm)?", 100, 200, 170, 1)
        weight = st.slider("What is your weight (kg)?", 20, 150, 50, 1)
        lifestyle = st.selectbox("Lifestyle: ", ["Sedentary (little to no exercise)", "Lightly Active (light exercise/sports 1-3 days per week)", "Moderately Active (moderate exercise/sports 3-5 days per week)", "Very Active (hard exercise/sports 6-7 days per week)", "Extra active (very hard exercise/sports and a physical job)"])
        enter = st.button("Enter")

    st.markdown("""<h1 style="text-align: center;">Result</h1>""", unsafe_allow_html=True)
    st.markdown("""---""", unsafe_allow_html=True)
    fill_in = st.markdown("""<h4 style="text-align: center; color: red">Please fill in the form on the left to get your results 😊</h4>""", unsafe_allow_html=True)

    if enter:
        if name:
            fill_in.empty()
            st.markdown("""<h2 style="text-align: center;">Hi {}! Here are your results:</h2>""".format(name), unsafe_allow_html=True)
            st.markdown("""<h4>Age: {}</h4>""".format(age), unsafe_allow_html=True)
            st.markdown("""<h4>Gender: {}</h4>""".format(gender), unsafe_allow_html=True)
            st.markdown("""<h4>Height: {} cm</h4>""".format(height), unsafe_allow_html=True)
            st.markdown("""<h4>Weight: {} kg</h4>""".format(weight), unsafe_allow_html=True)
            st.markdown("""<h4>Number of exercise sessions per week: {}</h4>""".format(lifestyle), unsafe_allow_html=True)

            
            engine = CalculateIntake()
            engine.reset()
            engine.declare(Gender(gender=gender))
            engine.declare(Age(age=age))
            engine.declare(Weight(weight=weight))
            engine.declare(Height(height=height))
            engine.declare(Lifestyle(lifestyle=lifestyle))
            engine.run()
        else:
            st.markdown("""<h4 style="text-align: center; color: red;">Please Enter Your Name 😊</h4>""", unsafe_allow_html=True)
        
    st.markdown("""---""", unsafe_allow_html=True)
    st.markdown("""<h1 style="text-align: center;">Health Tips</h1>""", unsafe_allow_html=True)
    st.markdown("""---""", unsafe_allow_html=True)
        
    engine = HealthTipsEngine()
    engine.reset()
    engine.declare(HealthTips())
    engine.run()
  

    st.markdown("""---""", unsafe_allow_html=True)
    st.markdown("""<h1 style="text-align: center;">Body Mass Index (BMI) Table</h1>""", unsafe_allow_html=True)

    engine = BMITableEngine()
    engine.reset()
    engine.declare(BMITable())
    engine.run()



    # Food suggestions (Extra: meal plan)
    # Health tips (does not depend on user's input)
