import streamlit as st

def app():
    # Insert Home Tab code here

    with st.sidebar:
        st.title("Let's get started!")
        name = st.text_input("How would you like us to address you?")
        age = st.slider("How old are you?", 10, 60, 18, 1)
        gender = st.selectbox("What is your gender?", ["Male", "Female"])
        height = st.slider("What is your height (cm)?", 100, 200, 170, 1)
        weight = st.slider("What is your weight (kg)?", 20, 150, 50, 1)
        lifestyle = st.selectbox("How many times do you exercise per week?", ["0 (Sedentary)", "1 - 2 (Lightly Active)", "3 - 5 (Moderately Active)", "6 - 7 (Very Active)"])
        submit = st.button("Submit")

    # if submit:
    #     st.markdown("""<h4 style="text-align: center;">User's Input:</h4>""", unsafe_allow_html=True)
    #     st.write("Name:", name)
    #     st.write("Age:", age)
    #     st.write("Gender:", gender)
    #     st.write("Height:", height)
    #     st.write("Weight:", weight)
    #     st.write("Lifestyle:", lifestyle)   





    # BMI (Extra: maybe can have a table to show the BMI range)
    # BMR
    # Required Protien Intake
    # Required Water Intake
    # Required Carbohydrate Intake
    # Required Vitamin and Mineral Intake
    # Food suggestions (Extra: meal plan)
    # Health tips (does not depend on user's input)
