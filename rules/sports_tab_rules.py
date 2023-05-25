import streamlit as st
from experta import Rule, Fact, KnowledgeEngine
from PIL import Image

# Insert rules of Sports Tab here
class TeamSportsType(Fact):
    """Info about the sport type"""
    pass

class IndividualSportsType(Fact):
    """Info about the sport type"""
    pass

# Team Sports Knowledge Engine
class TeamSports(KnowledgeEngine):
    @Rule(TeamSportsType(teamSports_type='Football'))
    def Football(self):
        st.markdown("""<h3 style="text-align: center;">Football</h3>""", unsafe_allow_html=True)
        image = Image.open('images/images_sport/football.jpeg')
        st.image(image, use_column_width=True)
        st.markdown("""<strong style="text-style: bold; font-size: 20px;">Football is the world's most popular team sport. It is played between two teams, each consisting of 11 players,
                    on a rectangular field. The objective of the game is to score goals by maneuvering a spherical ball into the opponent's goal, while defending one's own goal to prevent the opposing team from scoring. 
                    Football is known for its fast pace, skillful dribbling, precise passing, and strategic teamwork.
                    <br><br>
                    Rules and regulation of Football:
                    <ol>
                        <li > :red[Number of players:] A team consists of 11 players, including one goalkeeper.</li>
                        <li> :red[Duration of the Game:] The game is typically divided into two halves of 45 minutes each, with a halftime break of 15 minutes.</li>
                        <li> :red[Offside Rule:] A player is considered offside if they are nearer to the opponent's goal line than both the ball and the second-last defender when the ball is played to them.</li>
                        <li> :red[Fouls and Misconduct:] There are various fouls and misconduct that can occur during a game, such as tripping, pushing, holding, or using excessive force against an opponent. The referee may award free kicks, penalty kicks, or issue yellow or red cards depending on the severity of the offense.</li>
                        <li> :red[Penalties:] Penalties can be awarded for serious fouls or misconduct committed inside the penalty area. A penalty kick is taken from the penalty spot, 12 yards from the goal line, with only the goalkeeper defending the goal.</li>
                        <li> :red[Throw-in:] When the ball goes out of play over the touchline, a throw-in is awarded to the opposing team. The throw-in must be taken with both hands from behind and over the head. </li>
                        <li> :red[Goal Kick:] When the attacking team last touches the ball before it crosses the goal line, a goal kick is awarded to the defending team. The defending team's goalkeeper takes a kick from within the six-yard box. </li>
                        <li> :red[Corner Kick:] When the defending team last touches the ball before it crosses the goal line, a corner kick is awarded to the attacking team. The ball is placed in the corner arc nearest to where it went out of play and is kicked into play.</li>
                    </ol>
                    </strong>""", unsafe_allow_html=True)
    
    @Rule(TeamSportsType(teamSports_type='Basketball'))
    def Basketball(self):
        st.markdown("""<h3 style="text-align: center;">Basketball</h3>""", unsafe_allow_html=True)
        image = Image.open('images/images_sport/basketball.jpg')
        st.image(image, use_column_width=True)
        st.markdown("""<strong style="text-style: bold; font-size: 20px;">Basketball is a popular team sport played by two teams, each consisting of five players. 
                    The objective of the game is to score points by shooting the ball through the opponent's hoop while also preventing them from scoring in your team's hoop. 
                    Basketball is played on a rectangular court and is known for its fast-paced, high-scoring nature.
                    <br><br>
                    Rules and regulation of Basketball:
                    <ol>
                        <li> :red[Teams:] The positions typically include point guard, shooting guard, small forward, power forward, and center. </li>
                        <li> :red[Gameplay:] The game begins with a tip-off, where the referee throws the ball up into the air and two opposing players attempt to tap it to their teammates. The team in possession of the ball aims to advance it towards their opponent's hoop through dribbling (bouncing the ball while moving) and passing. Players can move the ball by dribbling, passing, or shooting. However, they must follow certain rules, such as dribbling violations (double dribble, carrying, etc.) and traveling (taking too many steps without dribbling). The shot clock is a timer that requires the offensive team to attempt a shot within a certain time limit (usually 24 seconds in professional basketball). Scoring can be done by shooting the ball into the opponent's hoop. A made basket inside the three-point line is worth two points, while a shot from beyond the three-point line counts for three points. Free throws are awarded for certain fouls and are worth one point each.</li>
                        <li> :red[Fouls and Violations:] Basketball has various fouls and violations that are penalized by the referees. Personal fouls include illegal physical contact, such as pushing, holding, or tripping an opponent. If a player commits too many fouls, they may be disqualified from the game. Technical fouls are given for unsportsmanlike behavior, such as arguing with the officials or using abusive language. Violations include traveling (taking too many steps without dribbling), double dribble (dribbling with both hands simultaneously), and shot clock violations, among others.</li>
                        <li> :red[Duration of the Game:] A standard basketball game consists of four quarters, each lasting 12 minutes in the NBA (National Basketball Association). In international competitions and some other leagues, the game may have different durations. If the game ends in a tie, additional periods of play, known as overtime, are added until a winner is determined.</li>
                    </ol>
                     </strong>""", unsafe_allow_html=True)
        
    @Rule(TeamSportsType(teamSports_type='Rugby'))
    def Rugby(self):
        st.markdown("""<h3 style="text-align: center;">Rugby</h3>""", unsafe_allow_html=True)
        image = Image.open('images/images_sport/rugby.jpg')
        st.image(image, use_column_width=True)
        st.markdown("""<strong style="text-style: bold; font-size: 20px;">Rugby is a popular contact sport that originated in England in the early 19th century. It is played with an oval-shaped ball and involves two teams of 15 players each (or 7 players in the case of Rugby Sevens) 
                    who aim to score points by advancing the ball and grounding it in the opponent's try zone or kicking it through the goalposts. Rugby is known for its physicality, strategic gameplay, and team camaraderie.
                    <br><br>
                    Rules and regulation of Rugby:
                    <ol>
                        <li> :red[Objective:] The objective of the game is to score more points than the opposing team by either scoring tries (worth 5 points), kicking conversions (2 points), penalty goals (3 points), or drop goals (3 points). </li>
                        <li> :red[Gameplay:]  The game is divided into two 40-minute halves, with a short halftime break. The teams attempt to move the ball forward by passing it backward or running with it while avoiding being tackled by the opposition. The ball can be kicked forward, but players must be behind the kicker at the time of the kick.</li>
                        <li> :red[Passing and Knock-on:] The ball can be passed between players in any direction but must be passed backward. If a player accidentally knocks the ball forward with their hand or arm, it results in a scrum for the opposing team.</li>
                        <li> :red[Tackling:] Players can tackle the ball carrier by grabbing them below the shoulders and bringing them to the ground. Tacklers must release the tackled player and allow them to release or pass the ball before contesting possession.</li>
                        <li> :red[Offside and Fouls:] Players must be behind the last foot of a ruck, maul, or tackle to remain onside. Fouls include dangerous tackles, obstruction, intentional knock-ons, and various forms of misconduct, resulting in penalties or yellow/red cards depending on the severity.</li>
                        <li> :red[Scrum:] A scrum is formed when there is an infringement, such as a forward pass or knock-on, or when the referee orders it. Eight players from each team bind together and contest for possession of the ball. The ball is fed into the scrum, and the two teams push against each other to gain control.</li>
                        <li> :red[Lineouts:] When the ball goes out of bounds, a lineout is awarded to the opposing team. Players from both teams line up perpendicular to the touchline, and the team awarded the lineout throws the ball back into play. Players lift teammates to catch or knock the ball back to their side.</li>
                        <li> :red[Rucks and Mauls:] When a player is tackled, a ruck is formed. Players from both teams bind together and try to gain possession of the ball. A maul occurs when the ball carrier is held by one or more opponents and players from both teams bind around them. In both cases, players must stay on their feet and not use their hands to play the ball.</li>
                    </ol>
                    </strong>""", unsafe_allow_html=True)
        
    @Rule(TeamSportsType(teamSports_type='Hockey'))
    def Hockey(self):
        st.markdown("""<h3 style="text-align: center;">Hockey</h3>""", unsafe_allow_html=True)
        image = Image.open('images/images_sport/hockey.jpg')
        st.image(image, use_column_width=True)
        st.markdown("""<strong style="text-style: bold; font-size: 20px;">Hockey is a fast-paced and exciting team sport played on ice, and it is widely popular in many countries around the world. The game is played between two teams, each consisting of six players, including a goaltender. 
                    The objective of the game is to score goals by shooting a small rubber disc called a puck into the opponent's net while defending your own net.
                    <br><br>
                    Rules and regulation of Hockey:
                    <ol>
                        <li> :red[Duration:] A standard field hockey game consists of two halves, with each half lasting 35 minutes at the international level. However, the duration can vary depending on the level of play and the specific competition. </li>
                        <li> :red[Starting the Game:] The game begins with a coin toss to determine which team starts with the ball. The team that wins the toss starts with a pass from the center of the field.</li>
                        <li> :red[Ball and Equipment:] Field hockey is played with a hard, spherical ball made of plastic or composite materials. Players use a hockey stick, which has a curved end, to hit the ball. Players are required to wear protective gear, including shin guards, mouthguards, and sometimes face masks. </li>
                        <li> :red[Fouls and Penalties:] Field hockey has specific rules regarding fouls and penalties. Fouls can include dangerous tackles, obstruction, intentional high sticks, and other infractions. Depending on the severity of the foul, penalties can range from a free hit for the opposing team to penalty corners or penalty strokes, where the attacking team has a chance to score from a set piece.</li>
                        <li> :red[Offsides:] Players must be in their own half of the field when the ball is hit into the attacking zone. If an attacking player precedes the ball into the attacking zone, they are considered offside. </li>
                        <li> :red[Free Hits:] When a foul occurs, the opposing team is awarded a free hit. The player taking the free hit must pass or hit the ball to restart play. Opposing players must be at least five yards away from the ball when the free hit is taken.</li>
                        <li> :red[Penalty Corners:] A penalty corner is awarded to the attacking team when a defensive foul occurs within the shooting circle or the defending team unintentionally hits the ball over their own goal line. During a penalty corner, the attacking team has a chance to score by taking a shot from the edge of the circle with defenders and the goalkeeper present.</li>
                        <li> :red[Scoring:] A goal is scored when the ball completely crosses the goal line between the goalposts and under the crossbar. The team with the most goals at the end of the game wins.</li>
                    </ol>
                    </strong>""", unsafe_allow_html=True)


# Individual Sports Knowledge Engine
class IndividualSports(KnowledgeEngine):
    @Rule(IndividualSportsType(individualSports_type='Swimming'))
    def Swimming(self):
        st.markdown("""<h3 style="text-align: center;">Swimming</h3>""", unsafe_allow_html=True)
        image = Image.open('images/images_sport/swimming.jpg')
        st.image(image, use_column_width=True)
        st.markdown("""<strong style="text-style: bold; font-size: 20px;">Swimming is a popular individual sport and recreational activity that involves propelling oneself through water using arm and leg movements. 
                    The sport encompasses different swimming strokes, each with its own technique and style. The main swimming strokes include freestyle, backstroke, breaststroke, and butterfly.
                    <br><br>
                    Advantages of Swimming:
                    <ol>
                        <li> :blue[Full-body workout:] Swimming engages multiple muscle groups, providing a comprehensive workout for the arms, legs, core, and back.</li>
                        <li> :blue[Cardiovascular fitness:] Swimming increases heart rate and improves cardiovascular endurance, enhancing overall cardiovascular health.</li>
                        <li> :blue[Low-impact exercise:] The buoyancy of water reduces stress on joints, making swimming a low-impact activity suitable for individuals with joint pain or injuries.</li>
                        <li> :blue[Improved strength and tone:] Regular swimming builds strength and muscle tone, promoting lean muscle development throughout the body.</li>
                        <li> :blue[Increased flexibility:] The range of motion required in swimming improves flexibility and joint mobility.</li>
                        <li> :blue[Weight management:] Swimming burns calories efficiently, aiding in weight loss and weight management goals. </li>
                        <li> :blue[Enhanced lung capacity:] Swimming involves controlled breathing, helping to improve lung function and respiratory efficiency. </li>
                        <li> :blue[Improved coordination and balance:] The rhythmic movements and coordination required in swimming enhance balance and body coordination.</li>
                        <li> :blue[Rehabilitation and injury recovery:] Swimming is a gentle form of exercise often used in rehabilitation programs to aid in injury recovery and improve physical function.</li>
                        <li> :blue[Suitable for all ages and fitness levels:] Swimming is an inclusive activity that can be enjoyed by people of all ages and varying fitness levels, from beginners to advanced athletes.</li>
                    </ol>  
                    Precautions of Swimming:
                    <ol>
                        <li> :red[Learn to swim:] It is essential to learn basic swimming skills and water safety techniques. Enroll in swimming lessons or seek guidance from a qualified instructor.</li>
                        <li> :red[Swim in designated areas:]  Choose swimming locations that are designated as safe for swimming, such as public pools, supervised beaches, or designated swimming areas in natural bodies of water.</li>
                        <li> :red[Observe water depth and conditions:] Be aware of the water depth and any potential hazards or currents present. Avoid swimming in unfamiliar or hazardous areas, including fast-flowing rivers, areas with submerged rocks, or locations with poor visibility.</li>
                        <li> :red[Supervise children:]  Keep a close eye on children when they are swimming, and provide them with appropriate flotation devices or swimming aids based on their skill level. Children should always be supervised by a responsible adult near water.</li>
                        <li> :red[Follow lifeguard instructions:] If swimming in an area with lifeguards, pay attention to their instructions and adhere to any posted signs or warnings.</li>
                        <li> :red[Be aware of weather conditions:] Pay attention to weather forecasts before swimming, especially in open water. Avoid swimming during storms, high winds, or thunderstorms, as these conditions can pose significant risks.</li>
                    </ol>
                    </strong>""", unsafe_allow_html=True)
    
    @Rule(IndividualSportsType(individualSports_type='Workout'))
    def Workout(self):
        st.markdown("""<h3 style="text-align: center;">Workout</h3>""", unsafe_allow_html=True)
        image = Image.open('images/images_sport/workout.jpg')
        st.image(image, use_column_width=True)
        st.markdown("""<strong style="text-style: bold; font-size: 20px;">A workout refers to a structured and intentional physical activity session aimed at improving fitness, strength, endurance, or overall health. Workouts can take various forms and can be customized based on individual goals, preferences, and fitness levels.
                    During a workout, individuals engage in specific exercises or activities designed to target different muscle groups, elevate heart rate, and challenge the body physically. Workouts can be performed at home, in a gym, or outdoors, depending on the available equipment and personal preferences.
                    <br><br>
                    Advantages of Workout:
                    <ol>
                        <li> :blue[Improved physical fitness:] Regular exercise helps improve overall physical fitness by increasing strength, endurance, flexibility, and cardiovascular health. It enhances muscle tone, promotes weight management, and improves body composition.</li>
                        <li> :blue[Increased energy levels:] Workouts stimulate the release of endorphins, which are natural chemicals that boost energy levels and improve mood. Regular exercise can leave you feeling more energized throughout the day.</li>
                        <li> :blue[Weight management:] Exercise plays a crucial role in maintaining a healthy weight or achieving weight loss goals. Workouts burn calories, increase metabolism, and promote fat loss, contributing to weight management.</li>
                        <li> :blue[Reduced risk of chronic diseases:] Regular physical activity reduces the risk of chronic diseases such as heart disease, type 2 diabetes, high blood pressure, and certain types of cancer. It helps maintain healthy blood pressure, cholesterol levels, and blood sugar regulation.</li>
                        <li> :blue[Improved cognitive function:] Physical activity has been linked to improved cognitive function, memory, and focus. Regular workouts can enhance mental clarity, concentration, and overall brain health.</li>
                        <li> :blue[Increased self-confidence:] Achieving fitness goals, improving physical abilities, and seeing progress in workouts can boost self-confidence and self-esteem. </li>
                        <li> :blue[Social benefits:] Group workouts or gym sessions provide opportunities for social interaction and can help build a supportive fitness community. </li>
                        <li> :blue[Longevity:] Regular exercise has been associated with increased longevity and a reduced risk of premature death.</li>
                        <li> :blue[Stronger immune system:] Consistent workouts can boost the immune system, reducing the likelihood of getting sick or experiencing frequent infections.</li>
                    </ol>  
                    Precautions of Workout:
                    <ol>
                        <li> :red[Consult with a healthcare professional:] If you have any underlying health conditions or concerns, it's advisable to consult with a healthcare professional before starting a new workout program. They can provide guidance on exercises that are safe and appropriate for your specific situation.</li>
                        <li> :red[Warm-up and cool-down:] Always begin your workout with a proper warm-up session to prepare your body for exercise. This can include light cardio exercises and dynamic stretching. Similarly, end your workout with a cool-down period to gradually bring your heart rate down and stretch your muscles.</li>
                        <li> :red[Use proper form and technique:] Learn and practice correct form and technique for each exercise to prevent injuries. If you're unsure about how to perform an exercise correctly, consider working with a qualified fitness professional who can guide you.</li>
                        <li> :red[Start gradually and progress slowly:] Start with lower intensity workouts and gradually increase the duration, intensity, or resistance over time. This allows your body to adapt and reduces the risk of overexertion or strain.</li>
                        <li> :red[Listen to your body:] Pay attention to your body's signals during a workout. If you experience pain, dizziness, or unusual discomfort, stop exercising and seek medical advice if necessary. Pushing through severe pain can lead to injuries.</li>
                        <li> :red[Use safety equipment:] If your workout involves activities like cycling, rollerblading, or weightlifting, wear appropriate safety equipment such as helmets, knee pads, or lifting belts to protect yourself from potential injuries.</li>
                    </ol>
                    </strong>""", unsafe_allow_html=True)
        
    @Rule(IndividualSportsType(individualSports_type='Cycling'))
    def Cycling(self):
        st.markdown("""<h3 style="text-align: center;">Cycling</h3>""", unsafe_allow_html=True)
        image = Image.open('images/images_sport/cycling.jpg')
        st.image(image, use_column_width=True)
        st.markdown("""<strong style="text-style: bold; font-size: 20px;">Cycling is a popular activity and mode of transportation that involves riding a bicycle.It can be performed on various terrains, including roads, trails, mountains, and indoor cycling studios. Cyclists can choose from different types of bicycles, such as road bikes, mountain bikes, hybrid bikes, or stationary bikes, depending on their preferences and intended use.
                    <br><br>
                    Advantages of Workout:
                    <ol>
                        <li> :blue[Cardiovascular fitness:] Cycling is an excellent aerobic exercise that raises the heart rate, improves cardiovascular health, and strengthens the heart and lungs. Regular cycling helps enhance endurance and overall cardiovascular fitness.</li>
                        <li> :blue[Low-impact exercise:] Cycling is a low-impact activity that puts less stress on the joints compared to high-impact exercises like running. It is suitable for individuals of different fitness levels, including those with joint issues or injuries.</li>
                        <li> :blue[Muscle strength and tone:] Cycling engages multiple muscle groups, including the legs, thighs, calves, glutes, and core. Regular cycling helps strengthen and tone these muscles, leading to improved lower body strength and stability.</li>
                        <li> :blue[Weight management:] Cycling is an effective calorie-burning exercise that can contribute to weight loss or weight management goals. The intensity and duration of cycling determine the number of calories burned during a ride.</li>
                        <li> :blue[Mental well-being:] Cycling offers mental and emotional benefits. It can help reduce stress, improve mood, and boost mental clarity and focus. Cycling outdoors also allows for a connection with nature, which can have a positive impact on mental well-being.</li>
                        <li> :blue[Joint mobility and flexibility:] Cycling involves a continuous range of motion, promoting joint mobility and flexibility. It helps maintain and improve joint health, especially in the knees, hips, and ankles.</li>
                        <li> :blue[Environmental sustainability:] Cycling is an eco-friendly mode of transportation as it does not produce harmful emissions or contribute to traffic congestion. Choosing to cycle instead of using a motor vehicle helps reduce carbon footprint and supports a greener environment. </li>
                        <li> :blue[Commuting and transportation:] Cycling can serve as an alternative mode of transportation, particularly for shorter distances. It offers convenience, promotes physical activity, and reduces reliance on motor vehicles, leading to cost savings and reduced traffic congestion.</li>
                        <li> :blue[Social interaction and community:] Cycling can be a social activity, allowing individuals to ride in groups or join cycling clubs. It provides an opportunity to connect with like-minded individuals, participate in group rides, and explore new routes or trails together.</li>
                        <li> :blue[Enjoyment and recreation:] Cycling can be a fun and enjoyable recreational activity, whether exploring scenic routes, going on cycling tours, or participating in organized cycling events or races.</li>
                    </ol>  
                    Precautions of Cycling:
                    <ol>
                        <li> :red[Wear a helmet:] Always wear a properly fitted helmet when cycling. A helmet can protect your head and reduce the risk of head injuries in case of a fall or collision.</li>
                        <li> :red[Follow traffic rules:] Obey traffic laws and regulations when cycling on roads. Ride in the same direction as traffic, use hand signals to indicate turns, and follow traffic signals and signs.</li>
                        <li> :red[Be visible:] Increase your visibility to motorists by wearing brightly colored or reflective clothing, especially when cycling in low-light conditions. Equip your bike with reflectors, lights, or strobes to ensure visibility to other road users.</li>
                        <li> :red[Be aware of your surroundings:] Pay attention to your surroundings and anticipate potential hazards. Watch out for parked cars, opening car doors, potholes, debris, or other obstacles on the road or trail.</li>
                        <li> :red[Maintain your bike:] Regularly inspect your bicycle for any mechanical issues, such as tire pressure, brake function, and chain condition. Ensure that all components are in proper working order before starting a ride.</li>
                        <li> :red[Signal your intentions:] Use hand signals to indicate your intentions to other road users. Signal when turning, changing lanes, or stopping to ensure that motorists and pedestrians are aware of your actions.</li>
                    </ol>
                    </strong>""", unsafe_allow_html=True)
        
    
        
        
        
        