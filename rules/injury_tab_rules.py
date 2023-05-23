import streamlit as st
from experta import Rule, Fact, KnowledgeEngine
from PIL import Image

# Injury Type Fact
class InjuryType(Fact):
    """Info about the injury type"""
    pass

# Common Injury Knowledge Engine
class CommonInjury(KnowledgeEngine):
    @Rule(InjuryType(injury_type='Sprain'))
    def sprain(self):
        st.markdown("""<h2 style="text-align: center;">Sprain</h2>""", unsafe_allow_html=True)
        image = Image.open('images/sprain.jpg')
        st.image(image, use_column_width=True)
        st.markdown("""<strong style="text-style: bold; font-size: 20px;">Sprains occur when the ligaments, which are pieces of tissue that connect two bones to one another in a joint, are overextended or torn. These ligaments play a crucial role in providing stability to the joints and preventing excessive movement. 
        Sprains can happen as a result of sudden twisting or wrenching movements, direct impact, or the application of excessive force to a joint. Common areas prone to sprains include the ankles, wrists, and knees. Symptoms of a sprain may include pain, swelling, bruising, limited range of motion, and difficulty 
        bearing weight on the affected joint.</strong>""", unsafe_allow_html=True)

    @Rule(InjuryType(injury_type='Strain'))
    def strain(self):
        st.markdown("""<h2 style="text-align: center;">Strain</h2>""", unsafe_allow_html=True)
        image = Image.open('images/strain.jpg')
        st.image(image, use_column_width=True)
        st.markdown("""<strong style="text-style: bold; font-size: 20px;">Strains refer to injuries that involve the overstretching or tearing of muscles or tendons. Tendons are thick, fibrous cords of tissue that connect muscles to bones. Strains often occur when muscles or tendons are subjected to sudden or 
        excessive stretching or forced contraction. Activities involving repetitive motions, improper technique, or insufficient warm-up can increase the risk of strains. Symptoms of a strain may include pain, muscle weakness, swelling, and difficulty 
        moving the affected muscle or joint.</strong>""", unsafe_allow_html=True)
        image = Image.open('images/strain.jpg')

    @Rule(InjuryType(injury_type='Knee Injury'))
    def knee_injury(self):
        st.markdown("""<h2 style="text-align: center;">Knee Injury</h2>""", unsafe_allow_html=True)
        image = Image.open('images/knee-injury.jpg')
        st.image(image, use_column_width=True)
        st.markdown("""<strong style="text-style: bold; font-size: 20px;">A knee injury encompasses various conditions that interfere with the normal movement and function of the knee joint. These injuries are commonly associated with sports activities, ranging from minor overstretching 
        or strain of the knee muscles and tissues to more severe tears. Factors contributing to knee injuries include sudden impact, twisting motions, repetitive stress, or inadequate conditioning. Symptoms of a knee injury may include pain, swelling, instability, difficulty walking or bearing weight, 
        and limited range of motion.</strong>""", unsafe_allow_html=True)

    @Rule(InjuryType(injury_type='Fractures'))
    def fracture(self):
        st.markdown("""<h2 style="text-align: center;">Factures</h2>""", unsafe_allow_html=True)
        image = Image.open('images/fracture.jpg')
        st.image(image, use_column_width=True)
        st.markdown("""<strong style="text-style: bold; font-size: 20px;">A fracture refers to a broken bone, which can range from a thin crack to a complete break. Bones can fracture in various ways, such as crosswise, lengthwise, in multiple places, or into many pieces. Fractures can occur 
        due to traumatic events, such as falls, accidents, or sports injuries. The severity of a fracture depends on the extent and location of the break. Common symptoms include pain, swelling, deformity, difficulty moving the affected area, and, in some cases, a visible 
        protrusion or abnormality.</strong>""", unsafe_allow_html=True)

    @Rule(InjuryType(injury_type='Muscle Cramps'))
    def swollen_muscles(self):
        st.markdown("""<h2 style="text-align: center;">Muscle Cramps</h2>""", unsafe_allow_html=True)
        image = Image.open('images/muscle-cramps.jpg')
        st.image(image, use_column_width=True)
        st.markdown("""<strong style="text-style: bold; font-size: 20px;">Muscle cramps are involuntary contractions or spasms of a muscle or group of muscles. They can occur suddenly and cause intense pain or discomfort. Muscle cramps can affect any muscle in the body but are most 
        commonly experienced in the legs, especially the calf muscles.</strong>""", unsafe_allow_html=True)

    @Rule(InjuryType(injury_type='Nose Injuries'))
    def nose_injury(self):
        st.markdown("""<h2 style="text-align: center;">Nose Injuries</h2>""", unsafe_allow_html=True)
        image = Image.open('images/nose-injury.jpg')
        st.image(image, use_column_width=True)
        st.markdown("""<strong style="text-style: bold; font-size: 20px;">Nose injuries involve damage to the skin or bone of the nose. They can result from a direct blow to the nose, commonly occurring during accidents, sports activities, or physical altercations. Nose injuries can 
        range from a blood nose, where the nose bleeds due to trauma, to a broken nose, which involves a fracture or displacement of the nasal bones. Symptoms may include pain, swelling, difficulty breathing, nosebleeds, and changes in the 
        shape or alignment of the nose.</strong>""", unsafe_allow_html=True)

    @Rule(InjuryType(injury_type='Bruises'))
    def bruise(self):
        st.markdown("""<h2 style="text-align: center;">Bruises</h2>""", unsafe_allow_html=True)
        image = Image.open('images/bruise.jpeg')
        st.image(image, use_column_width=True)
        st.markdown("""<strong style="text-style: bold; font-size: 20px;">Bruises are a common type of skin injury that results in discoloration. When blood vessels deep beneath the skin are damaged, blood leaks out and collects near the surface, causing the characteristic black-and-blue mark. 
        Bruises can occur due to impacts or trauma, such as bumps, falls, or injuries. The appearance of a bruise may change over time, transitioning from red or purple to green or yellow as the body reabsorbs the trapped blood. While bruises typically heal on their own, severe or recurrent bruising 
        may require medical attention.</strong>""", unsafe_allow_html=True)

    @Rule(InjuryType(injury_type='Cuts and Abrasions'))
    def cut_and_abrasion(self):
        st.markdown("""<h2 style="text-align: center;">Cuts and Abrasions</h2>""", unsafe_allow_html=True)
        image = Image.open('images/cut-and-abrasion.jpg')
        st.image(image, use_column_width=True)
        st.markdown("""<strong style="text-style: bold; font-size: 20px;">Cuts and abrasions refer to skin wounds that involve the rubbing or tearing off of skin tissue. They are commonly caused by falls, accidents, or contact with sharp objects. Areas such as the knees and hands are particularly 
        prone to cuts and abrasions due to their exposure and vulnerability. These injuries can vary in severity, from minor surface scratches to deeper cuts that may require stitches. Proper cleaning, disinfection, and bandaging are important for preventing infection and promoting 
        healing.</strong>""", unsafe_allow_html=True)

    @Rule(InjuryType(injury_type='Dental Damage'))
    def dental_damange(self):
        st.markdown("""<h2 style="text-align: center;">Dental Damage</h2>""", unsafe_allow_html=True)
        image = Image.open('images/dental-damage.jpg')
        st.image(image, use_column_width=True)
        st.markdown("""<strong style="text-style: bold; font-size: 20px;">Dental damage encompasses injuries to the teeth, gums, or jawbones. It can occur due to a direct blow to the mouth, face, or jaw, or indirect forces like falls or automobile accidents. Dental damage can manifest as cracked or 
        broken teeth, dislodged teeth, injuries to the gums, or fractures of the jawbones. Symptoms may include tooth pain, sensitivity, bleeding gums, difficulty biting or chewing, and visible abnormalities in the teeth or mouth. Prompt dental evaluation and treatment are necessary to prevent 
        further complications.</strong>""", unsafe_allow_html=True)

    @Rule(InjuryType(injury_type='Dislocations'))
    def discolation(self):
        st.markdown("""<h2 style="text-align: center;">Dislocations</h2>""", unsafe_allow_html=True)
        image = Image.open('images/dislocation.jpeg')
        st.image(image, use_column_width=True)
        st.markdown("""<strong style="text-style: bold; font-size: 20px;">Dislocations are injuries that involve the displacement of bones at a joint, causing them to be forced from their normal positions. This typically occurs as a result of significant impact, trauma, or excessive force applied 
        to a joint. Dislocations can affect various joints in the body, such as the shoulder, elbow, or knee. Symptoms may include severe pain, swelling, deformity, limited mobility, and instability in the affected joint. Prompt medical attention is crucial to properly realign the joint and prevent 
        additional damage.</strong>""", unsafe_allow_html=True)

    
# ------------------------------------------------------------
    
# Treatment Type Fact
class TreatmentType(Fact):
    """Info about the treatment type"""
    pass

# Treatment Knowledge Engine
class Treatment(KnowledgeEngine):
    @Rule(TreatmentType(treatment_type='First Aid for Sprains, Strains and Joint Injuries'))
    def first_aid_for_sprains_strains_and_joint_injuries(self):
        st.markdown("""<h2 style="text-align: center;">First Aid for Sprains, Strains and Joint Injuries</h2>""", unsafe_allow_html=True)
        image = Image.open('images/first-aid-for-sprains-strains-and-joint-injuries.png')
        st.image(image, use_column_width=True)
        st.markdown("""<strong style="text-style: bold; font-size: 20px;"><span style="color: red;">R.I.C.E</span> method. This treatment method is helpful for mild sports injuries. For best results, follow the RICE method within the first 24 to 36 hours after the injury. It can help reduce swelling 
        and prevent additional pain and bruising in the early days after a sports injury.
        <br><br>
        Here's the step-by-step guide on the RICE method:
        <br>
        <br>→ <span style="color: red;">Rest</span> – Keep the injured area supported and avoid using for 48-72 hours.
        <br>→ <span style="color: red;">Ice</span> – Apply ice to the injured area for 20 minutes every two hours for the first 48-72 hours.
        <br>→ <span style="color: red;">Compression</span> – Apply a firm elastic bandage over the area, extending above and below the painful site.
        <br>→ <span style="color: red;">Elevation</span> – Raise the injured area above the level of the heart at all times.
        </strong>""", unsafe_allow_html=True)
        
    @Rule(TreatmentType(treatment_type='First Aid for Nose Bleeds'))
    def first_aid_for_nose_bleeds(self):
        st.markdown("""<h2 style="text-align: center;">First Aid for Nose Bleeds</h2>""", unsafe_allow_html=True)
        image = Image.open('images/first-aid-for-nose-bleeds.jpg')
        st.image(image, use_column_width=True)
        st.markdown("""<strong style="text-style: bold; font-size: 20px;">
        Here's the step-by-step guide on how to stop a nose bleed:
        <br><br>→ Stop the activity.
        <br>→ Sit with your head leaning forward.
        <br>→ Pinch your nostrils together and breathe through your mouth.
        <br>→ Hold your nose for at least 10 minutes.
        <br>→ If bleeding continues past 30 minutes, seek medical advice.</strong>""", unsafe_allow_html=True)

    @Rule(TreatmentType(treatment_type='First Aid for Disldodged Teeth'))
    def first_aid_for_dislodged_teeth(self):
        st.markdown("""<h2 style="text-align: center;">First Aid for Disldodged Teeth</h2>""", unsafe_allow_html=True)
        image = Image.open('images/first-aid-for-dislodged-teeth.jpg')
        st.image(image, use_column_width=True)
        st.markdown("""<strong style="text-style: bold; font-size: 20px;">
        Here's the step-by-step guide on how to handle a dislodged tooth:
        <br><br>→ Handle your tooth by the top or crown only — don't touch the roots.
        <br>→ Inspect the crown and root to determine if any portion of either appears to be missing or fractured.
        <br>→ Don't rub the tooth or scrape it to remove debris. This damages the root surface, making the tooth less likely to survive.
        <br>→ If your tooth has dirt or foreign material on it, gently rinse your tooth briefly — no more than 10 seconds — in a bowl of lukewarm tap water to remove the debris. Don't hold it under running water, because too much tap water could kill the cells on the root surface that help reattach the tooth.
        <br>→ Try to put your tooth back in the socket. If it doesn't go all the way into place, bite down slowly and gently on gauze or a moistened paper towel to help keep it in place. Hold the tooth in place until you see your dentist.
        <br>→ If you can't put your tooth back in the socket, immediately place it between your cheek and gum, or in cold milk or your own saliva. Or use an over-the-counter product that preserves a knocked-out tooth, such as those approved by the American Dental Association, if you have quick access to it.
        <br>→ Get emergency dental care. If your dentist's office isn't open, go to the emergency room.</strong>""", 
        unsafe_allow_html=True)
    
    @Rule(TreatmentType(treatment_type='Emergency Situation'))
    def emergency_situation(self):
        st.markdown("""<h2 style="text-align: center;">Emergency Situation</h2>""", unsafe_allow_html=True)
        image = Image.open('images/emergency-situation.png')
        st.image(image, use_column_width=True)
        st.markdown("""<strong style="text-style: bold; font-size: 20px;">
        Call ambulance for:
        <br><br>→ Prolonged Loss of Consciousness
        <br>→ Neck or Spine Injuries
        <br>→ Broken Bones
        <br>→ Injuries to the Head or Face
        <br>→ Eye Injuries
        <br>→ Abdominal Injuries
        <br>→ Difficulty Breathing
        <br>→ Dizziness
        <br>→ Severe Pain
        <br>→ Severe Bleeding
        </strong>""", unsafe_allow_html=True)
        

# ------------------------------------------------------------

# Prevention Type Fact
class PreventionType(Fact):
    """Info about the prevention type"""
    pass


# Prevention Knowledge Engine
class Prevention(KnowledgeEngine):
    @Rule(PreventionType(prevention_type='Always Warm Up Beforehand'))
    def warm_up(self):
        st.markdown("""<h2 style="text-align: center;">Always Warm Up Beforehand</h2>""", unsafe_allow_html=True)
        image = Image.open('images/warm-up.jpg')
        st.image(image, use_column_width=True)
        st.markdown("""<strong style="text-style: bold; font-size: 20px;">The purpose of warming up before engaging in sports and other related 
        activities is to prepare yourself physically for the more strenuous activities that you will be putting your body through afterwards. By doing so, it will enhance your 
        blood flow and increase muscle elasticity, ultimately reducing the risk of sports injuries.
        <br><br>Here's a list of warm up exercises that you can do before engaging in sports and other related activities:
        <ul>
            <li>Stretching</li>
            <li>Fast-paced Walking</li>
            <li>Arm Swings</li>
            <li>Leg Swings</li>
            <li>Squats</li>
            <li>High Knees</li>
        </ul>
        </strong>""", unsafe_allow_html=True)

    @Rule(PreventionType(prevention_type='Exercise Regularly'))
    def exercise_regularly(self):
        st.markdown("""<h2 style="text-align: center;">Exercise Regularly</h2>""", unsafe_allow_html=True)
        image = Image.open('images/exercise-regularly.jpg')
        st.image(image, use_column_width=True)
        st.markdown("""<strong style="text-style: bold; font-size: 20px;">Contrary to popular belief, avoiding exercise entirely can actually increase your risk of sports injuries. 
        Regular exercise stands as one of the most effective methods for preventing such injuries. When you engage in exercise, you actively strengthen your muscles, resulting in increased flexibility and agility. 
        By exercising regularly, you can ensure your body is always ready for exercise and reduce the likelihood of common injuries.
        Regular exercise not only strengthens muscles but also enhances flexibility, improves balance and coordination, promotes healthy bones and joints, boosts cardiovascular fitness, 
        aids in weight management, and contributes to overall mental well-being. By incorporating exercise into your routine, you significantly reduce the risk of sports-related injuries and create a foundation for 
        a healthier and more enjoyable sports experience.</strong>""", unsafe_allow_html=True)

    @Rule(PreventionType(prevention_type='Do not Push Your Body Beyond Its Limits'))
    def push_body(self):
        st.markdown("""<h2 style="text-align: center;">Do not Push Your Body Beyond Its Limits</h2>""", unsafe_allow_html=True)
        image = Image.open('images/push-body.jpg')
        st.image(image, use_column_width=True)
        st.markdown("""<strong style="text-style: bold; font-size: 20px;">When you push your body beyond its limits, either by overtraining or engaging in activities without proper preparation, you significantly increase 
        the likelihood of experiencing sports injuries. It's crucial to recognize the importance of listening to your body and respecting its signals. If you do sustain an injury, it is essential to prioritize your recovery and 
        give your body the care it needs to heal effectively—avoid the temptation to rush the process and return to sports prematurely.
        <br><br>
        During the recovery phase, it is crucial to follow the guidance of healthcare professionals, such as doctors, physical therapists, or sports trainers. They can provide specific instructions tailored to your injury to ensure 
        that you follow the appropriate treatment plan and rehabilitation exercises. By adhering to their recommendations, you give your body the necessary time and resources to regain strength and functionality.
        </strong>""", unsafe_allow_html=True)

    @Rule(PreventionType(prevention_type='Use the Proper Technique'))
    def proper_technique(self):
        st.markdown("""<h2 style="text-align: center;">Use the Proper Technique</h2>""", unsafe_allow_html=True)
        image = Image.open('images/proper-technique.jpg')
        st.image(image, use_column_width=True)
        st.markdown("""<strong style="text-style: bold; font-size: 20px;">Learning the proper way to move during your sport or activity is essential for maximizing performance and minimizing the risk of injuries. Each sport or activity 
        has its own set of movements, techniques, and body positions that are considered correct or optimal. Understanding and practicing the correct technique and form is crucial for executing movements efficiently and effectively. Proper 
        technique not only enhances performance but also reduces the strain on joints, muscles, and ligaments, reducing the risk of overuse injuries or acute trauma. For example, in some sports, bending your knees at the right time can help 
            avoid an injury to your spine or hips.</strong>""", unsafe_allow_html=True)
        
    @ Rule(PreventionType(prevention_type='Have the Proper Equipment'))
    def proper_equipment(self):
        st.markdown("""<h2 style="text-align: center;">Have the Proper Equipment</h2>""", unsafe_allow_html=True)
        image = Image.open('images/proper-equipment.jpg')
        st.image(image, use_column_width=True)
        st.markdown("""<strong style="text-style: bold; font-size: 20px;">Having the proper equipment is essential for preventing sports injuries. The right equipment can help protect your body from the impact of falls, collisions, or other 
        potential hazards associated with sports and physical activities. By providing an additional layer of safety, proper equipment significantly reduces the risk of severe injuries and ensures a safer and more enjoyable sports 
        experience.</strong>""", unsafe_allow_html=True)

    @Rule(PreventionType(prevention_type='Cool Down'))
    def cool_down(self):
        st.markdown("""<h2 style="text-align: center;">Cool Down</h2>""", unsafe_allow_html=True)
        image = Image.open('images/cool-down.jpg')
        st.image(image, use_column_width=True)
        st.markdown("""<strong style="text-style: bold; font-size: 20px;">Cooling down after exercise is just as crucial as warming up beforehand, as it allows your body to transition from a state of exertion to a state of rest in a gradual and controlled manner. 
        During a cool-down, your heart rate gradually decreases and your body allows the cardiovascular system to return to its resting state. It also aids in the removal of metabolic waste products, such as lactic acid, from your muscles, reducing the 
        likelihood of muscle soreness and promoting faster recovery. Additionally, cooling down with stretching exercises helps relax and lengthen your muscles, preventing tightness and imbalances. Cooling down after exercise is just as crucial as warming up beforehand, 
        as it allows your body to transition from a state of exertion to a state of rest in a gradual and controlled manner. During a cool-down, your heart rate gradually decreases, allowing your cardiovascular system to return to its resting state. It also aids in the 
        removal of metabolic waste products, such as lactic acid, from your muscles, reducing the likelihood of muscle soreness and promoting faster recovery. Additionally, cooling down with stretching exercises helps relax and lengthen your muscles, preventing tightness and imbalances.
        <br><br>
        Here's a list of cool down exercises that you can do after engaging in sports and other related activities:
        <ul>
            <li>Walking</li>
            <li>Stretching</li>
            <li>Yoga</li>
            <li>Deep Breathing</li>
        </ul>
        </strong>""", unsafe_allow_html=True)

    @Rule(PreventionType(prevention_type='Resume Activity Slowly'))
    def resume_activity(self):
        st.markdown("""<h2 style="text-align: center;">Resume Activity Slowly</h2>""", unsafe_allow_html=True)
        image = Image.open('images/resume-activity.jpg')
        st.image(image, use_column_width=True)
        st.markdown("""<strong style="text-style: bold; font-size: 20px;">After recovering from an injury, it is crucial to approach the resumption of physical activity with caution and a gradual progression. Rushing back into full-fledged activity too soon can jeopardize your recovery and 
        increase the risk of re-injury. Instead, taking a slow and gradual approach allows your body to heal and adapt, and reduce the likelihood of setbacks. By gradually increasing the intensity, duration, and complexity of your activities, you give your body 
        time to rebuild strength, flexibility, and coordination in the affected area. This gradual return also allows you to closely monitor your body's response by making adjustments as needed and ensuring a safe and successful 
        recovery.</strong>""", unsafe_allow_html=True)
        


