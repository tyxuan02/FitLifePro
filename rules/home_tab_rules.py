import streamlit as st
from experta import Rule, Fact, DefFacts, MATCH, KnowledgeEngine

# Insert rules of Home Tab here
class Gender(Fact):
    """Info about the user's gender"""
    pass

class Age(Fact):
    """Info about the user's age"""
    pass

class Weight(Fact):
    """Info about the user's weight"""
    pass

class Height(Fact):
    """Info about the user's height"""
    pass

class Lifestyle(Fact):
    """Info about the user's lifestyle"""
    pass

class BMR(Fact):
    """Info about the user's BMR"""
    pass

class CalorieIntake(Fact):
    """Info about the user's required calorie intake"""
    pass

# Rules for BMI
class CalculateIntake(KnowledgeEngine):
    @Rule(Weight(weight=MATCH.weight), Height(height=MATCH.height), salience=10)
    def calculate_BMI(self, weight, height):
        BMI_result = weight / (height/100)**2
        
        if BMI_result < 18.5:
            st.markdown("""<h4 style:"display: inline;">BMI: {:.2f} <span style="color: red;">(You are underweight)</span></h4>""".format(BMI_result), unsafe_allow_html=True)
        elif BMI_result >= 18.5 and BMI_result < 25:
            st.markdown("""<h4 style:"display: inline;">BMI: {:.2f} <span style="color: green;">(You are healthy)</span></h4>""".format(BMI_result), unsafe_allow_html=True)
        elif BMI_result >= 25 and BMI_result < 30:
            st.markdown("""<h4 style:"display: inline;">BMI: {:.2f} <span style="color: orange;">(You are overweight)</span></h4>""".format(BMI_result), unsafe_allow_html=True)
        else:
            st.markdown("""<h4 style:"display: inline;">BMI: {:.2f} <span style="color: red;">(You are obese)</span></h4>""".format(BMI_result), unsafe_allow_html=True)
    
    @Rule(Weight(weight=MATCH.weight), Height(height=MATCH.height), Age(age = MATCH.age), Gender(gender=MATCH.gender), salience=9)
    def calculate_BMR(self, weight, height, age, gender):
        if gender == "Male":
            BMR_result = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
        else:
            BMR_result = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)

        BMR_result = round(BMR_result, 2)
        self.declare(BMR(BMR=BMR_result))
        st.markdown("""<h4>BMR: {}</h4>""".format(BMR_result), unsafe_allow_html=True)
    
    # Rules for Required Calorie Intake
    @Rule(Lifestyle(lifestyle=MATCH.lifestyle), BMR(BMR=MATCH.BMR), salience=8)
    def calculate_calorie(self, lifestyle, BMR):
        if lifestyle == "Sedentary (little to no exercise)":
            CalorieIntake_result = BMR * 1.2
        elif lifestyle == "Lightly Active (light exercise/sports 1-3 days per week)":
            CalorieIntake_result = BMR * 1.375
        elif lifestyle == "Moderately Active (moderate exercise/sports 3-5 days per week)":
            CalorieIntake_result = BMR * 1.55
        elif lifestyle == "Very Active (hard exercise/sports 6-7 days per week)":
            CalorieIntake_result = BMR * 1.725
        else:
            CalorieIntake_result = BMR * 1.9
        
        self.declare(CalorieIntake(CalorieIntake=CalorieIntake_result))
        # Convert to kJ
        CalorieIntakeInkJ = CalorieIntake_result * 4.184 / 1000
        st.markdown("""<h4>Required Calorie Intake: {:.2f} cal/day ({:.2f} kJ/day)</h4>""".format(CalorieIntake_result, CalorieIntakeInkJ), unsafe_allow_html=True)

    # Rules for Required Protein Intake
    @Rule(Weight(weight=MATCH.weight), Lifestyle(lifestyle=MATCH.lifestyle), Age(age=MATCH.age), salience=7)
    def calculate_protein(self, weight, lifestyle, age):
        if age <= 30:
            if lifestyle == "Sedentary (little to no exercise)":
                ProteinIntake = weight * 0.8
            elif lifestyle == "Lightly Active (light exercise/sports 1-3 days per week)":
                ProteinIntake = weight * 1.0
            elif lifestyle == "Moderately Active (moderate exercise/sports 3-5 days per week)":
                ProteinIntake = weight * 1.2
            elif lifestyle == "Very Active (hard exercise/sports 6-7 days per week)":
                ProteinIntake = weight * 1.4
            else:
                ProteinIntake = weight * 1.6
        else:
            ProteinIntake = weight * 0.9
        
        st.markdown("""<h4>Required Protein Intake: {:.2f} g/day</h4>""".format(ProteinIntake), unsafe_allow_html=True)
    
    # Rules for Required Water Intake
    @Rule(Weight(weight=MATCH.weight), Lifestyle(lifestyle=MATCH.lifestyle), salience=6)
    def calculate_water(self, weight, lifestyle):
        if lifestyle == "Sedentary (little to no exercise)":
            WaterIntake = weight * 0.025
        elif lifestyle == "Lightly Active (light exercise/sports 1-3 days per week)":
            WaterIntake = weight * 0.03
        elif lifestyle == "Moderately Active (moderate exercise/sports 3-5 days per week)":
            WaterIntake = weight * 0.035
        elif lifestyle == "Very Active (hard exercise/sports 6-7 days per week)":
            WaterIntake = weight * 0.04
        else:
            WaterIntake = weight * 0.045
        
        st.markdown("""<h4>Required Water Intake: {:.2f} L/day</h4>""".format(WaterIntake), unsafe_allow_html=True)

    # Rules for Required Carbohydrate Intake
    @Rule(CalorieIntake(CalorieIntake=MATCH.CalorieIntake), salience=5)
    def calculate_carbohydrate(self, CalorieIntake):
        CarbohydrateIntake = (CalorieIntake / 2) / 4
        st.markdown("""<h4>Required Carbohydrate Intake: {:.2f} g/day</h4>""".format(CarbohydrateIntake), unsafe_allow_html=True)
            
        
        



    
          