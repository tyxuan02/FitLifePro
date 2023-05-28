import streamlit as st
from experta import Rule, Fact, MATCH, KnowledgeEngine

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

class CalculateIntake(KnowledgeEngine):
    # Rules for BMI
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
    
    # Rules for BMR
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
            WaterIntake = weight * 0.04
        elif lifestyle == "Lightly Active (light exercise/sports 1-3 days per week)":
            WaterIntake = weight * 0.042
        elif lifestyle == "Moderately Active (moderate exercise/sports 3-5 days per week)":
            WaterIntake = weight * 0.048
        elif lifestyle == "Very Active (hard exercise/sports 6-7 days per week)":
            WaterIntake = weight * 0.052
        else:
            WaterIntake = weight * 0.056
        
        st.markdown("""<h4>Required Water Intake: {:.2f} L/day</h4>""".format(WaterIntake), unsafe_allow_html=True)

    # Rules for Required Carbohydrate Intake
    @Rule(CalorieIntake(CalorieIntake=MATCH.CalorieIntake), salience=5)
    def calculate_carbohydrate(self, CalorieIntake):
        CarbohydrateIntake = (CalorieIntake / 2) / 4
        st.markdown("""<h4>Required Carbohydrate Intake: {:.2f} g/day</h4>""".format(CarbohydrateIntake), unsafe_allow_html=True)



class HealthTips(Fact):
    """Info about the user's health tips"""
    pass

# Rules for Health Tips
class HealthTipsEngine(KnowledgeEngine):
    @Rule(HealthTips(), salience=15)
    def balanced_diet(self):
        st.markdown("""<div style="margin: 30px">
            <h3>Eat a Balanced Diet</h3>
            <p style="font-size: 20px">Focus on consuming a variety of whole foods, including fruits, vegetables, lean proteins, whole grains, and healthy fats. Aim for a balanced mix of macronutrients (carbohydrates, proteins, and fats) in each meal.</p>
        </div>""", unsafe_allow_html=True)
    
    @Rule(HealthTips(), salience=14)
    def control_portion(self):
        st.markdown("""<div style="margin: 30px">
            <h3>Control Portion for Every Meal</h3>
            <p style="font-size: 20px">Be mindful of portion sizes to avoid overeating. Use smaller plates, bowls, and cups to help control your portions.</p>
        </div>""", unsafe_allow_html=True)

    @Rule(HealthTips(), salience=13)
    def limit_processed_food_and_added_sugar(self):
        st.markdown("""<div style="margin: 30px">
            <h3>Limit Processed Food and Added Sugar</h3>
            <p style="font-size: 20px">Limit processed foods, such as pre-made meals, snacks, and convenience foods. They are usually high in calories, added sugars, artificial ingredients and unhealthy fats.</p>
        </div>""", unsafe_allow_html=True)
    
    @Rule(HealthTips(), salience=12)
    def prioritize_fruits_and_vegetables(self):
        st.markdown("""<div style="margin: 30px">
            <h3>Prioritize Fruits and Vegetables</h3>
            <p style="font-size: 20px">Fruits and vegetables are rich in vitamins, minerals, and fiber, which can support your immune system and overall health. They are also low in calories and fat. Aim to fill half your plate with fruits and vegetables.</p>
        </div>""", unsafe_allow_html=True)

    @Rule(HealthTips(), salience=11)
    def engage_in_regular_physical_activity(self):
        st.markdown("""<div style="margin: 30px">
            <h3>Engage in Regular Physical Activity</h3>
            <p style="font-size: 20px">Regular physical activity has many health benefits, including helping you burn calories, reducing your risk of chronic diseases, and improving your mood and sleep.
            Aim for at least 150 minutes of moderate-intensity aerobic exercise or 75 minutes of vigorous exercise per week. Find activities you enjoy, such as walking, swimming, dancing, or cycling, 
            and make them a regular part of your routine.</p>
        </div>""", unsafe_allow_html=True)

    @Rule(HealthTips(), salience=10)
    def get_enough_sleep(self):
        st.markdown("""<div style="margin: 30px">
            <h3>Get Enough Sleep</h3>
            <p style="font-size: 20px">Getting enough sleep is vital for your health. Many studies have found that not getting enough sleep may increase the risk of obesity, diabetes, heart disease, and depression.
            Prioritize getting 7-9 hours of quality sleep each night. Establish a regular sleep schedule and create a conducive sleep environment to improve your sleep quality.</p>
        </div>""", unsafe_allow_html=True)

    @Rule(HealthTips(), salience=9)
    def manage_stree(self):
        st.markdown("""<div style="margin: 30px">
            <h3>Manage Stress</h3>
            <p style="font-size: 20px">Stress can have negative effects on your health. It can raise your blood pressure, increase your risk of heart disease, and negatively impact your immune system.
            Find ways to reduce stress in your life. Try relaxation techniques such as meditation, yoga, or deep breathing or spend time doing activities you enjoy.</p>
        </div>""", unsafe_allow_html=True)

    @Rule(HealthTips(), salience=8)
    def stay_socially_connected(self):
        st.markdown("""<div style="margin: 30px">
            <h3>Stay Socially Connected</h3>
            <p style="font-size: 20px">Social connections can help protect your health as you age. Spend time with loved ones, engage in activities with others, and seek support when needed.</p>
        </div>""", unsafe_allow_html=True)

    @Rule(HealthTips(), salience=7)
    def practice_mindful_eating(self):
        st.markdown("""<div style="margin: 30px">
            <h3>Practice Mindful Eating</h3>
            <p style="font-size: 20px">Mindful eating is a powerful tool to gain control of your eating habits. It can cause weight loss, reduce binge eating, and make you feel better.
            To practice mindful eating, minimize distractions by turning off the TV and putting down your phone. Eat slowly and pay attention to the taste, texture, and aroma of your food.
            Try to eat without judgment and listen to your body.</p>
        </div>""", unsafe_allow_html=True)

    @Rule(HealthTips(), salience=6)
    def do_not_smoke(self):
        st.markdown("""<div style="margin: 30px">
            <h3>Do Not Smoke</h3>
            <p style="font-size: 20px">Smoking is a major cause of heart disease, cancer, and lung disease. Quitting smoking can help improve your health. It is never too late to quit.</p>
        </div>""", unsafe_allow_html=True)
    
    @Rule(HealthTips(), salience=5)
    def limit_alcohol_consumption(self):
        st.markdown("""<div style="margin: 30px">
            <h3>Limit Alcohol Consumption</h3>
            <p style="font-size: 20px">Drinking too much alcohol can have many negative effects on your health. It can increase your risk of many conditions, including heart disease, obesity, and cancer.
            Establish clear limits for your alcohol consumption and avoid drinking when you are upset or stressed.</p>
        </div>""", unsafe_allow_html=True)
    
    @Rule(HealthTips(), salience=4)
    def incorporate_strength_training(self):
        st.markdown("""<div style="margin: 30px">
            <h3>Incorporate Strength Training</h3>
            <p style="font-size: 20px">Strength training is a great way to improve your health and fitness. It can help you maintain bone density and muscle mass, both of which decline as you age.    
            Incorporate strength training into your exercise routine 2-3 times per week. Focus on all major muscle groups, including your arms, legs, shoulders, back, hips, and abdomen.</p>
        </div>""", unsafe_allow_html=True)

    @Rule(HealthTips(), salience=3)
    def practice_moderation(self):
        st.markdown("""<div style="margin: 30px">
            <h3>Practice Moderation</h3>
            <p style="font-size: 20px">Moderation is key to a healthy diet. This does not mean you have to avoid foods you enjoy. Instead, it is about eating smaller portions less frequently.
            For example, you could limit fried foods to a few times per week instead of every day. Choose smaller portions of foods high in fat, sugar, and sodium and larger portions of nutrient-dense foods.</p>
        </div>""", unsafe_allow_html=True)



class BMITable(Fact):
    """Info about the user's health tips"""
    pass

# Rules for BMI Table
class BMITableEngine(KnowledgeEngine):
    @Rule(BMITable())
    def BMI_Table(self):
        st.markdown("""<table style="width:100%; text-align: center; font-size: 20px; text-style: bold">
                        <br>
                        <tr>
                            <th>BMI</th>
                            <th>Weight Status</th>
                        </tr>
                        <tr>
                            <td>Below 18.5</td>
                            <td>Underweight</td>
                        </tr>
                        <tr>
                            <td>18.5 - 24.9</td>
                            <td>Healthy</td>
                        </tr>
                        <tr>
                            <td>25.0 - 29.9</td>
                            <td>Overweight</td>
                        </tr>
                        <tr>
                            <td>30.0 and above</td>
                            <td>Obese</td>
                        </tr>
                    </table>""", unsafe_allow_html=True)



    
          