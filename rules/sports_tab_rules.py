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
    
    @Rule(TeamSportsType(teamSports_type='Baseball'))
    def Baseball(self):
        st.markdown("""<h3 style="text-align: center;">Baseball</h3>""", unsafe_allow_html=True)
        image = Image.open('images/images_sport/baseball.jpg')
        st.image(image, use_column_width=True)
        st.markdown("""<strong style="text-style: bold; font-size: 20px;">Baseball is a popular sport that is played between two teams consisting of nine players each. 
                    The objective of baseball is for one team to score more runs than the opposing team within a designated number of innings. 
                    A run is scored when a player successfully completes a circuit around four bases: first base, second base, third base, and finally home plate.
                    The team that is on offense tries to score runs by hitting the ball and running around the bases, while the team on defense attempts to prevent the offense from scoring by fielding the ball and making outs.
                    <br><br>
                    Rules and regulation of Baseball:
                    <ol>
                        <li> :red[Playing Field:] Baseball is played on a diamond-shaped field, with four bases positioned at the corners. The distance between each base is 90 feet (27.4 meters). The outfield, beyond the bases, is typically covered in grass. </li>
                        <li> :red[Innings:] A baseball game consists of nine innings, with each team getting a turn to bat and a turn to field. If the game is tied after nine innings, extra innings are played until there is a winner. </li>
                        <li> :red[Batting:] The batting team sends one player, known as the batter, to the home plate. The pitcher from the opposing team throws the ball towards the batter, who tries to hit it into the field of play. The batter must stay within the batter's box while attempting to hit the ball. </li>
                        <li> :red[Strikes, Balls, and Outs:] The pitcher throws pitches, and the batter aims to hit them. If the batter swings and misses, it's called a strike. If the batter doesn't swing, but the pitch is within the strike zone (the area over home plate between the batter's shoulders and knees), it's also called a strike. If the batter receives four balls (pitches outside the strike zone), they are awarded a walk and advance to first base. </li>
                        <li> :red[Scoring:] A run is scored when a base runner successfully touches all four bases, including home plate, without being put out. The team with the most runs at the end of the game wins. </li>
                        <li> :red[Base Running:] After hitting the ball, the batter becomes a base runner and must run counterclockwise around the bases. Runners can be tagged out by fielders holding the ball and touching the runner before they reach a base. Runners can also be forced out if a fielder touches the base before they arrive, and there are no other bases available.</li>
                        <li> :red[Foul Territory: ] The area outside the foul lines, extending beyond the first and third baselines and beyond the outfield fences, is called foul territory. If a batter hits the ball into foul territory, it's a foul ball, and generally, the count remains unchanged. However, if a foul ball is caught by a fielder before touching the ground, the batter is out. </li>
                    </ol>
                    </strong>""", unsafe_allow_html=True)
        
    @Rule(TeamSportsType(teamSports_type='Volleyball'))
    def Volleyball(self):
        st.markdown("""<h3 style="text-align: center;">Volleyball</h3>""", unsafe_allow_html=True)
        image = Image.open('images/images_sport/volleyball.jpg')
        st.image(image, use_column_width=True)
        st.markdown("""<strong style="text-style: bold; font-size: 20px;">Volleyball is a team sport played by two teams on a rectangular court separated by a net. 
                    It is a fast-paced and dynamic game that involves players using their hands or arms to hit a ball over the net, with the objective of scoring points and preventing the opposing team from doing the same.
                    <br><br>
                    Rules and regulation of Volleyball:
                    <ol>
                        <li> :red[Scoring:] The objective of volleyball is to score points by making the ball touch the ground within the opponent's court or by forcing the opponent into an error. A team scores a point if they successfully ground the ball on the opponent's court or if the opposing team commits a fault. The first team to reach 25 points (with a two-point advantage) wins the set. Matches are typically best-of-five sets. </li>
                        <li> :red[Serve:]The game begins with a serve, where a player from behind the end line serves the ball into the opponent's court. The server must hit the ball over the net and into the receiving team's court. The serve must clear the net and land within the boundaries of the court. </li>
                        <li> :red[Rally:] After the serve, the teams engage in a rally, where the ball is played back and forth between them. Each team has a maximum of three touches to return the ball over the net. Typical techniques include a forearm pass (bump), overhead pass (set), or an attacking hit. </li>
                        <li> :red[Ball In Play:] The ball is in play from the moment it is served until it lands out of bounds, hits an obstruction, or a fault is committed. Players must avoid touching the net, stepping over the centerline, or committing other violations to keep the ball in play. </li>
                        <li> :red[Libero:] In international and advanced-level volleyball, teams can utilize a libero player who specializes in defensive skills. The libero wears a different-colored jersey and has specific rules, such as being limited to back-row play and not being allowed to serve, attack the ball above the net, or rotate to the front row. </li>
                        <li> :red[Faults and Violations:] Various faults and violations can occur during a game, resulting in points awarded to the opposing team. These include serving into the net, hitting the ball out of bounds, touching the net, double-touching the ball, and committing foot faults while serving.</li>
                        <li> :red[Substitutions:] Teams are allowed to make substitutions during the game, typically during dead ball situations. Substituted players may replace the serving player or take other positions on the court. </li>
                    </ol>
                    </strong>""", unsafe_allow_html=True)

    @Rule(TeamSportsType(teamSports_type='Handball'))
    def Handball(self):
        st.markdown("""<h3 style="text-align: center;">Handball</h3>""", unsafe_allow_html=True)
        image = Image.open('images/images_sport/handball.jpg')
        st.image(image, use_column_width=True)
        st.markdown("""<strong style="text-style: bold; font-size: 20px;">Handball is a fast-paced team sport played between two teams of seven players each, with six outfield players and one goalkeeper. 
                    The objective of handball is to score goals by throwing the ball into the opponent's goal while preventing the opposing team from doing the same. 
                    <br><br>
                    Rules and regulation of Handball:
                    <ol>
                        <li> :red[Scoring:] The objective of handball is to score goals. A goal is scored when the ball completely crosses the goal line, between the goalposts and below the crossbar, without any rule violations. The team that scores the most goals within the designated time wins the match. </li>
                        <li> :red[Duration of the Game:] A handball match is typically played in two halves of 30 minutes each, with a 10 to 15-minute halftime break. However, the duration can vary based on the level of play and competition. If the game ends in a draw, it may go into overtime or a shootout to determine the winner. </li>
                        <li> :red[Ball Possession:] The team in possession of the ball tries to move it towards the opponent's goal through passes, dribbling, and player movement. Players can hold the ball for a maximum of three seconds before they must pass, bounce, or shoot it. Dribbling is allowed, similar to basketball, but contact with the floor should be made alternately with each hand. </li>
                        <li> :red[Passing:] Players can pass the ball to their teammates using various throwing techniques, such as overhead passes, bounce passes, or sidearm throws. However, players are not allowed to hold the ball for more than three steps or three seconds without dribbling or releasing it. </li>
                        <li> :red[Fouls and Penalties:] Handball has rules to prevent unfair play and ensure player safety. Fouls can result from actions such as holding, pushing, tripping, or charging into opponents. When a foul is committed, the opposing team is awarded a free throw or a penalty throw, depending on the severity and location of the foul. </li>
                        <li> :red[Goalkeeper: ] The goalkeeper has a unique role in handball, positioned in front of the goal to block shots. They have additional privileges and restrictions compared to outfield players. For example, goalkeepers can touch the ball with any part of their body within the goal area, and they can participate in the game as an outfield player beyond that area. </li>
                        <li> :red[Substitutions:] Teams are allowed to make substitutions during the game, typically during breaks in play or stoppages. Substituted players enter and exit the game through a designated substitution area on the sideline, ensuring a smooth flow of the game. </li>
                    </ol>
                    </strong>""", unsafe_allow_html=True)

# Individual Sports Knowledge Engine
class IndividualSports(KnowledgeEngine):
    @Rule(IndividualSportsType(individualSports_type='Swimming'))
    def Swimming(self):
        st.markdown("""<h3 style="text-align: center;">Swimming</h3>""", unsafe_allow_html=True)
        image = Image.open('images/images_sport/swimming.jpg')
        st.image(image, use_column_width=True)
        st.markdown(
            """
            <strong style="text-style: bold; font-size: 20px;">Swimming is a popular individual sport and recreational activity that involves propelling oneself through water using arm and leg movements. The sport encompasses different swimming strokes, each with its own technique and style. The main swimming strokes include freestyle, backstroke, breaststroke, and butterfly.
            <br/><br/>
            <span style="font-size:20px;"><strong>Advantages of Swimming:</strong></span>
            <ol>
                <li><span style="color:blue;"><strong>Full-body workout:</span> Swimming engages multiple muscle groups, providing a comprehensive workout for the arms, legs, core, and back.</strong></li>
                <li><span style="color:blue;"><strong>Cardiovascular fitness:</span> Swimming increases heart rate and improves cardiovascular endurance, enhancing overall cardiovascular health.</strong></li>
                <li><span style="color:blue;"><strong>Low-impact exercise:</span> The buoyancy of water reduces stress on joints, making swimming a low-impact activity suitable for individuals with joint pain or injuries.</strong></li>
                <li><span style="color:blue;"><strong>Improved strength and tone:</span> Regular swimming builds strength and muscle tone, promoting lean muscle development throughout the body.</strong></li>
                <li><span style="color:blue;"><strong>Increased flexibility:</span> The range of motion required in swimming improves flexibility and joint mobility.</strong></li>
                <li><span style="color:blue;"><strong>Weight management:</span> Swimming burns calories efficiently, aiding in weight loss and weight management goals. </strong></li>
                <li><span style="color:blue;"><strong>Enhanced lung capacity:</span> Swimming involves controlled breathing, helping to improve lung function and respiratory efficiency. </strong></li>
                <li><span style="color:blue;"><strong>Improved coordination and balance:</span> The rhythmic movements and coordination required in swimming enhance balance and body coordination.</strong></li>
                <li><span style="color:blue;"><strong>Rehabilitation and injury recovery:</span> Swimming is a gentle form of exercise often used in rehabilitation programs to aid in injury recovery and improve physical function.</strong></li>
                <li><span style="color:blue;"><strong>Suitable for all ages and fitness levels:</span> Swimming is an inclusive activity that can be enjoyed by people of all ages and varying fitness levels, from beginners to advanced athletes.</strong></li>
            </ol>  
            <br/>
            <span style="font-size:20px;"><strong>Precautions of Swimming:</strong></span>
                <ol>
                    <li><span style="color:red;"><strong>Learn to swim:</span> It is essential to learn basic swimming skills and water safety techniques. Enroll in swimming lessons or seek guidance from a qualified instructor.</li>
                    <li><span style="color:red;"><strong>Swim in designated areas:</span>  Choose swimming locations that are designated as safe for swimming, such as public pools, supervised beaches, or designated swimming areas in natural bodies of water.</li>
                    <li><span style="color:red;"><strong>Observe water depth and conditions:</span> Be aware of the water depth and any potential hazards or currents present. Avoid swimming in unfamiliar or hazardous areas, including fast-flowing rivers, areas with submerged rocks, or locations with poor visibility.</li>
                    <li><span style="color:red;"><strong>Supervise children:</span>  Keep a close eye on children when they are swimming, and provide them with appropriate flotation devices or swimming aids based on their skill level. Children should always be supervised by a responsible adult near water.</li>
                    <li><span style="color:red;"><strong>Follow lifeguard instructions:</span> If swimming in an area with lifeguards, pay attention to their instructions and adhere to any posted signs or warnings.</li>
                    <li><span style="color:red;"><strong>Be aware of weather conditions:</span> Pay attention to weather forecasts before swimming, especially in open water. Avoid swimming during storms, high winds, or thunderstorms, as these conditions can pose significant risks.</li>
                </ol>
            """, 
            unsafe_allow_html=True)
    
    @Rule(IndividualSportsType(individualSports_type='Workout'))
    def Workout(self):
        st.markdown("""<h3 style="text-align: center;">Workout</h3>""", unsafe_allow_html=True)
        image = Image.open('images/images_sport/workout.jpg')
        st.image(image, use_column_width=True)
        st.markdown(
            """
            <strong style="text-style: bold; font-size: 20px;">A workout refers to a structured and intentional physical activity session aimed at improving fitness, strength, endurance, or overall health. Workouts can take various forms and can be customized based on individual goals, preferences, and fitness levels. During a workout, individuals engage in specific exercises or activities designed to target different muscle groups, elevate heart rate, and challenge the body physically. Workouts can be performed at home, in a gym, or outdoors, depending on the available equipment and personal preferences.
            <br/><br/>
            <span style="font-size:20px;"><strong>Advantages of Workout:</strong></span>
            <ol>
                <li><span style="color:blue;"><strong>Improved physical fitness:</span> Regular exercise helps improve overall physical fitness by increasing strength, endurance, flexibility, and cardiovascular health. It enhances muscle tone, promotes weight management, and improves body composition.</strong></li>
                <li><span style="color:blue;"><strong>Increased energy levels:</span> Workouts stimulate the release of endorphins, which are natural chemicals that boost energy levels and improve mood. Regular exercise can leave you feeling more energized throughout the day.</strong></li>
                <li><span style="color:blue;"><strong>Weight management:</span> Exercise plays a crucial role in maintaining a healthy weight or achieving weight loss goals. Workouts burn calories, increase metabolism, and promote fat loss, contributing to weight management.</strong></li>
                <li><span style="color:blue;"><strong>Reduced risk of chronic diseases:</span> Regular physical activity reduces the risk of chronic diseases such as heart disease, type 2 diabetes, high blood pressure, and certain types of cancer. It helps maintain healthy blood pressure, cholesterol levels, and blood sugar regulation.</strong></li>
                <li><span style="color:blue;"><strong>Improved cognitive function:</span> Physical activity has been linked to improved cognitive function, memory, and focus. Regular workouts can enhance mental clarity, concentration, and overall brain health.</strong></li>
                <li><span style="color:blue;"><strong>Increased self-confidence:</span> Achieving fitness goals, improving physical abilities, and seeing progress in workouts can boost self-confidence and self-esteem. </strong></li>
                <li><span style="color:blue;"><strong>Social benefits:</span> Group workouts or gym sessions provide opportunities for social interaction and can help build a supportive fitness community. </strong></li>
                <li><span style="color:blue;"><strong>Longevity:</span> Regular exercise has been associated with increased longevity and a reduced risk of premature death.</strong></li>
                <li><span style="color:blue;"><strong>Stronger immune system:</span> Consistent workouts can boost the immune system, reducing the likelihood of getting sick or experiencing frequent infections.</strong></li>
            </ol> 
            <br/> 
            <span style="font-size:20px;"><strong>Precautions of Workout:</strong></span>
            <ol>
                <li><span style="color:red;"><strong>Consult with a healthcare professional:</span> If you have any underlying health conditions or concerns, it's advisable to consult with a healthcare professional before starting a new workout program. They can provide guidance on exercises that are safe and appropriate for your specific situation.</strong></li>
                <li><span style="color:red;"><strong>Warm-up and cool-down:</span> Always begin your workout with a proper warm-up session to prepare your body for exercise. This can include light cardio exercises and dynamic stretching. Similarly, end your workout with a cool-down period to gradually bring your heart rate down and stretch your muscles.</strong></li>
                <li><span style="color:red;"><strong>Use proper form and technique:</span> Learn and practice correct form and technique for each exercise to prevent injuries. If you're unsure about how to perform an exercise correctly, consider working with a qualified fitness professional who can guide you.</strong></li>
                <li><span style="color:red;"><strong>Start gradually and progress slowly:</span> Start with lower intensity workouts and gradually increase the duration, intensity, or resistance over time. This allows your body to adapt and reduces the risk of overexertion or strain.</strong></li>
                <li><span style="color:red;"><strong>Listen to your body:</span> Pay attention to your body's signals during a workout. If you experience pain, dizziness, or unusual discomfort, stop exercising and seek medical advice if necessary. Pushing through severe pain can lead to injuries.</strong></li>
                <li><span style="color:red;"><strong>Use safety equipment:</span> If your workout involves activities like cycling, rollerblading, or weightlifting, wear appropriate safety equipment such as helmets, knee pads, or lifting belts to protect yourself from potential injuries.</strong></li>                 </ol>
            </ol>
            """, 
            unsafe_allow_html=True)
        

    @Rule(IndividualSportsType(individualSports_type='Cycling'))
    def Cycling(self):
        st.markdown("""<h3 style="text-align: center;">Cycling</h3>""", unsafe_allow_html=True)
        image = Image.open('images/images_sport/cycling.jpg')
        st.image(image, use_column_width=True)

        st.markdown(
            """
            <strong style="text-style: bold; font-size: 20px;">Cycling is a popular activity and mode of transportation that involves riding a bicycle.It can be performed on various terrains, including roads, trails, mountains, and indoor cycling studios. Cyclists can choose from different types of bicycles, such as road bikes, mountain bikes, hybrid bikes, or stationary bikes, depending on their preferences and intended use.</strong>
            <br/><br/>
            <span style="font-size:20px;"><strong>Advantages of Cycling:</strong></span>
            <ol>
                <li><span style="color:blue;"><strong>Cardiovascular fitness:</span> Cycling is an excellent aerobic exercise that raises the heart rate, improves cardiovascular health, and strengthens the heart and lungs. Regular cycling helps enhance endurance and overall cardiovascular fitness.</strong></li>
                <li><span style="color:blue;"><strong>Low-impact exercise:</span> Cycling is a low-impact activity that puts less stress on the joints compared to high-impact exercises like running. It is suitable for individuals of different fitness levels, including those with joint issues or injuries.</strong></li>
                <li><span style="color:blue;"><strong>Muscle strength and tone:</span> Cycling engages multiple muscle groups, including the legs, thighs, calves, glutes, and core. Regular cycling helps strengthen and tone these muscles, leading to improved lower body strength and stability.</strong></li>
                <li><span style="color:blue;"><strong>Weight management:</span> Cycling is an effective calorie-burning exercise that can contribute to weight loss or weight management goals. The intensity and duration of cycling determine the number of calories burned during a ride.</strong></li>
                <li><span style="color:blue;"><strong>Mental well-being:</span> Cycling offers mental and emotional benefits. It can help reduce stress, improve mood, and boost mental clarity and focus. Cycling outdoors also allows for a connection with nature, which can have a positive impact on mental well-being.</strong></li>
                <li><span style="color:blue;"><strong>Joint mobility and flexibility:</span> Cycling involves a continuous range of motion, promoting joint mobility and flexibility. It helps maintain and improve joint health, especially in the knees, hips, and ankles.</strong></li>
                <li><span style="color:blue;"><strong>Environmental sustainability:</span> Cycling is an eco-friendly mode of transportation as it does not produce harmful emissions or contribute to traffic congestion. Choosing to cycle instead of using a motor vehicle helps reduce carbon footprint and supports a greener environment.</strong></li>
                <li><span style="color:blue;"><strong>Commuting and transportation:</span> Cycling can serve as an alternative mode of transportation, particularly for shorter distances. It offers convenience, promotes physical activity, and reduces reliance on motor vehicles, leading to cost savings and reduced traffic congestion.</strong></li>
                <li><span style="color:blue;"><strong>Social interaction and community:</span> Cycling can be a social activity, allowing individuals to ride in groups or join cycling clubs. It provides an opportunity to connect with like-minded individuals, participate in group rides, and explore new routes or trails together.</strong></li>
                <li><span style="color:blue;"><strong>Enjoyment and recreation:</span> Cycling can be a fun and enjoyable recreational activity, whether exploring scenic routes, going on cycling tours, or participating in organized cycling events or races.</strong></li>
            </ol>
            <br/>
            <span style="font-size:20px;"><strong>Precautions of Cycling:</strong></span>
            <ol>
                <li><span style="color:red;"><strong>Wear a helmet:</span> Always wear a properly fitted helmet when cycling. A helmet can protect your head and reduce the risk of head injuries in case of a fall or collision.</strong></li>
                <li><span style="color:red;"><strong>Follow traffic rules:</span> Obey traffic laws and regulations when cycling on roads. Ride in the same direction as traffic, use hand signals to indicate turns, and follow traffic signals and signs.</strong></li>
                <li><span style="color:red;"><strong>Be visible:</span> Increase your visibility to motorists by wearing brightly colored or reflective clothing, especially when cycling in low-light conditions. Equip your bike with reflectors, lights, or strobes to ensure visibility to other road users.</strong></li>
                <li><span style="color:red;"><strong>Be aware of your surroundings:</span> Pay attention to your surroundings and anticipate potential hazards. Watch out for parked cars, opening car doors, potholes, debris, or other obstacles on the road or trail.</strong></li>
                <li><span style="color:red;"><strong>Maintain your bike:</span> Regularly inspect your bicycle for any mechanical issues, such as tire pressure, brake function, and chain condition. Ensure that all components are in proper working order before starting a ride.</strong></li>
                <li><span style="color:red;"><strong>Signal your intentions:</span> Use hand signals to indicate your intentions to other road users. Signal when turning, changing lanes, or stopping to ensure that motorists and pedestrians are aware of your actions.</strong></li>
            </ol>
            """,
            unsafe_allow_html=True
        )

        
    @Rule(IndividualSportsType(individualSports_type='Jogging'))
    def Jogging(self):
        st.markdown("""<h3 style="text-align: center;">Jogging</h3>""", unsafe_allow_html=True)
        image = Image.open('images/images_sport/jogging.jpg')
        st.image(image, use_column_width=True)

        st.markdown(
            """
            <strong style="text-style: bold; font-size: 20px;">Jogging is a form of running that is characterized by a slower pace than sprinting or fast running. It typically involves a continuous, rhythmic motion of running at a pace that allows for sustained effort without excessive fatigue. Jogging can be tailored to individual fitness levels, making it suitable for beginners as well as experienced runners.</strong>
            <br/><br/>
            <span style="font-size:20px;"><strong>Advantages of Jogging:</strong></span>
            <ol>
                <li><span style="color:blue;"><strong>Cardiovascular fitness:</span> Jogging is an effective aerobic exercise that elevates heart rate, improves cardiovascular health, and strengthens the heart and lungs. Regular jogging helps increase stamina, endurance, and overall cardiovascular fitness.</strong></li>
                <li><span style="color:blue;"><strong>Bone health:</span> Weight-bearing exercises like jogging help strengthen bones and reduce the risk of osteoporosis. The impact of each step during jogging stimulates bone growth and increases bone density.</strong></li>
                <li><span style="color:blue;"><strong>Muscle strength and endurance:</span> Jogging engages multiple muscle groups, including the legs, core, and upper body. It helps develop leg muscles, improve lower body strength, and enhance overall muscular endurance.</strong></li>
                <li><span style="color:blue;"><strong>Weight management:</span> Jogging is an excellent calorie-burning activity that can contribute to weight loss or weight management goals. It helps burn calories and fat, making it an effective exercise for maintaining a healthy body weight.</strong></li>
                <li><span style="color:blue;"><strong>Mental well-being:</span> Jogging is known to have positive effects on mental health. It releases endorphins, the feel-good hormones, which can reduce stress, improve mood, boost self-esteem, and alleviate symptoms of depression and anxiety.</strong></li>
                <li><span style="color:blue;"><strong>Convenience and accessibility:</span> Jogging requires minimal equipment and can be done almost anywhere. It offers the flexibility to choose different routes, terrains, and times of the day to fit into busy schedules.</strong></li>
                <li><span style="color:blue;"><strong>Outdoor connection:</span> Jogging outdoors allows individuals to connect with nature and enjoy fresh air and natural surroundings. It can provide a sense of relaxation and escape from the pressures of daily life.</strong></li>
                <li><span style="color:blue;"><strong>Social engagement:</span> Jogging can be a solo activity or a social one. Joining jogging groups or participating in organized running events can provide opportunities for social interaction, motivation, and a sense of community.</strong></li>
            </ol>
            <br/>
            <span style="font-size:20px;"><strong>Precautions of Jogging:</strong></span>
            <ol>
                <li><span style="color:red;"><strong>Warm-up:</span> Begin each jogging session with a warm-up to prepare the muscles and joints for the activity. Perform light cardiovascular exercises and dynamic stretching to increase blood flow and warm up the muscles.</strong></li>
                <li><span style="color:red;"><strong>Proper footwear:</span> Wear appropriate running shoes that provide cushioning, support, and a proper fit. This helps prevent foot and ankle injuries and ensures a comfortable running experience.</strong></li>
                <li><span style="color:red;"><strong>Gradual progression:</span> Start with a manageable pace and distance, and gradually increase the intensity and duration of your jogging sessions over time. This allows the body to adapt and reduces the risk of overuse injuries.</strong></li>
                <li><span style="color:red;"><strong>Listen to your body:</span> Pay attention to your body's signals during jogging. If you experience pain, excessive fatigue, or any discomfort, adjust your pace or take a break. Pushing through severe pain can lead to injuries.</strong></li>
                <li><span style="color:red;"><strong>Hydration:</span> Stay hydrated by drinking water before, during, and after your jog, especially in hot or humid conditions. Maintain adequate fluid intake to prevent dehydration.</strong></li>
                <li><span style="color:red;"><strong>Rest and recovery:</span> Allow your body time to rest and recover between jogging sessions. Incorporate rest days into your routine to prevent overtraining and promote muscle repair.</strong></li>
            </ol>
            """,
            unsafe_allow_html=True
        )

    @Rule(IndividualSportsType(individualSports_type='Hiking'))
    def Hiking(self):
        st.markdown("""<h3 style="text-align: center;">Hiking</h3>""", unsafe_allow_html=True)
        image = Image.open('images/images_sport/hiking.jpg')
        st.image(image, use_column_width=True)

        st.markdown(
            """
            <strong style="text-style: bold; font-size: 20px;">Hiking is an outdoor activity that involves walking on trails or paths through natural landscapes such as mountains, forests, valleys, or parks.It has vary levels of difficulty and terrain. It can range from leisurely walks on well-marked trails to more challenging treks that require endurance and navigation skills.</strong>
            <br/><br/>
            <span style="font-size:20px;"><strong>Advantages of Hiking:</strong></span>
            <ol>
                <li><span style="color:blue;"><strong>Physical exercise:</span> Hiking provides a moderate to vigorous physical workout. It engages major muscle groups, such as the legs, core, and glutes, and helps improve cardiovascular fitness, endurance, and overall strength.</strong></li>
                <li><span style="color:blue;"><strong>Nature immersion:</span> Hiking allows individuals to explore and immerse themselves in natural surroundings. It provides an opportunity to appreciate the beauty of landscapes, observe wildlife, and experience the tranquility and serenity of the outdoors.</strong></li>
                <li><span style="color:blue;"><strong>Stress relief and mental well-being:</span> Being in nature and engaging in physical activity during a hike can help reduce stress levels and improve mental well-being. Hiking provides a break from the demands of daily life and offers a chance to disconnect and recharge.</strong></li>
                <li><span style="color:blue;"><strong>Fresh air and natural environment:</span> Hiking enables individuals to breathe in fresh air and experience the therapeutic benefits of spending time in a natural environment. It can improve respiratory health and enhance overall feelings of well-being.</strong></li>
                <li><span style="color:blue;"><strong>Exploration and adventure:</span> Hiking opens up possibilities for exploration and adventure. It allows individuals to discover new trails, experience different terrains, and challenge themselves physically and mentally.</strong></li>
                <li><span style="color:blue;"><strong>Social interaction:</span> Hiking can be enjoyed alone as a solitary activity or with others, providing an opportunity for social interaction and shared experiences. It can be a great way to spend time with friends, family, or hiking groups.</strong></li>
                <li><span style="color:blue;"><strong>Outdoor education and appreciation:</span> Hiking can provide opportunities for learning about the environment, flora, fauna, and local history. Many hiking trails have informational signs or interpretive materials that offer insights into the natural and cultural aspects of the area.</strong></li>
            </ol>
            <br/>
            <span style="font-size:20px;"><strong>Precautions of Hiking:</strong></span>
            <ol>
                <li><span style="color:red;"><strong>Plan and prepare:</span> Research and plan your hike beforehand, considering factors such as trail difficulty, weather conditions, and necessary equipment. Inform others about your plans and estimated return time.</strong></li>
                <li><span style="color:red;"><strong>Dress appropriately:</span> Wear comfortable, moisture-wicking clothing and suitable footwear for the terrain. Dress in layers to accommodate changes in temperature and weather conditions.</strong></li>
                <li><span style="color:red;"><strong>Stay hydrated and nourished:</span> Carry an adequate supply of water and snacks to stay hydrated and energized during your hike. Be mindful of the duration and intensity of your hike to plan accordingly.</strong></li>
                <li><span style="color:red;"><strong>Carry essentials:</span> Bring necessary equipment and supplies, such as a map, compass, first aid kit, sunscreen, insect repellent, and a fully charged mobile phone or communication device. Pack according to the requirements of the hike and the potential challenges you may encounter.</strong></li>
                <li><span style="color:red;"><strong>Follow trail markers and regulations:</span> Stay on designated trails, follow trail markers, and respect any posted regulations or guidelines. Leave no trace by packing out any waste and respecting the natural environment.</strong></li>
                <li><span style="color:red;"><strong>Know your limits:</span> Choose a hike that matches your fitness level and experience. Be aware of your physical capabilities and adjust your pace or route accordingly. It's important to be prepared for the challenges you may face during the hike.</strong></li>
            </ol>
            """,
            unsafe_allow_html=True
        )
        
    @Rule(IndividualSportsType(individualSports_type='Martial arts'))
    def MartialArts(self):
        st.markdown("""<h3 style="text-align: center;">Martial arts</h3>""", unsafe_allow_html=True)
        image = Image.open('images/images_sport/martial arts.jpg')
        st.image(image, use_column_width=True)

        st.markdown(
            """
            <strong style="text-style: bold; font-size: 20px;">Martial arts originated in various parts of the world, with different cultures and traditions influencing their development. Each martial art has its own unique techniques, training methods, and philosophies. Some well-known martial arts include Karate, Taekwondo, Judo, Jiu-Jitsu, Kung Fu, Muay Thai, Boxing, and Capoeira, among many others. Martial arts training typically involves a combination of striking techniques (punches, kicks, knees, elbows), grappling and submission techniques, joint locks, throws, and defensive maneuvers. These techniques are often practiced in controlled environments, such as training halls or dojos, under the guidance of skilled instructors.</strong>
            <br/><br/>
            <span style="font-size:20px;"><strong>Advantages of Martial Arts:</strong></span>
            <ol>
                <li><span style="color:blue;"><strong>Self-defense:</span> Martial arts training equips individuals with the knowledge and skills to protect themselves in potentially dangerous situations. Techniques are practiced to develop the ability to respond effectively and efficiently to physical threats.</strong></li>
                <li><span style="color:blue;"><strong>Physical fitness and conditioning:</span> Martial arts training provides a comprehensive workout that improves strength, flexibility, agility, coordination, and cardiovascular endurance. Training sessions often involve warm-up exercises, drills, sparring, and conditioning exercises.</strong></li>
                <li><span style="color:blue;"><strong>Mental focus and discipline:</span> Martial arts cultivate mental discipline and concentration. Training requires focused attention, as practitioners strive to execute techniques with precision and timing. Discipline is fostered through adherence to training routines, etiquette, and codes of conduct.</strong></li>
                <li><span style="color:blue;"><strong>Self-confidence and self-esteem:</span> As practitioners progress in their martial arts journey, they gain confidence in their abilities and develop a sense of self-assurance. Martial arts training promotes self-esteem by setting and achieving goals, overcoming challenges, and pushing personal boundaries.</strong></li>
                <li><span style="color:blue;"><strong>Stress relief and emotional well-being:</span> Engaging in martial arts can provide a healthy outlet for stress and tension. The physical activity and mental focus help reduce anxiety, improve mood, and promote emotional well-being.</strong></li>
                <li><span style="color:blue;"><strong>Cultural appreciation and personal growth:</span> Many martial arts have deep cultural roots and historical significance. Practicing martial arts offers an opportunity to appreciate and respect different cultures and traditions. It can also serve as a vehicle for personal growth, encouraging self-reflection and continuous self-improvement.</strong></li>
                <li><span style="color:blue;"><strong>Competitive sport:</span> Several martial arts have developed into competitive sports with organized tournaments and competitions. These events provide an avenue for practitioners to showcase their skills, test their abilities, and engage in friendly competition.</strong></li>
            </ol>
            <br/>
            <span style="font-size:20px;"><strong>Precautions of Martial Arts:</strong></span>
            <ol>
                <li><span style="color:red;"><strong>Warm-up and stretching:</span> Always start your training session with a proper warm-up and stretching routine. This helps prepare your muscles, joints, and cardiovascular system for the physical demands of martial arts training, reducing the risk of injury.</strong></li>
                <li><span style="color:red;"><strong>Proper technique and form:</span> Focus on learning and executing techniques with proper form and technique. This not only maximizes the effectiveness of your movements but also minimizes the risk of strain, sprains, or other injuries caused by improper body mechanics.</strong></li>
                <li><span style="color:red;"><strong>Hydration and nutrition:</span> Stay hydrated by drinking water before, during, and after training. Maintain a balanced diet to support your energy levels, muscle recovery, and overall health.</strong></li>
                <li><span style="color:red;"><strong>Gradual progression:</span> Progress in your martial arts training gradually. Avoid pushing yourself too hard or attempting advanced techniques before you have mastered the basics. Gradual progression allows your body to adapt, reducing the risk of overuse injuries or burnout.</strong></li>
                <li><span style="color:red;"><strong>Protective gear:</span> When engaging in sparring or contact-based training, use appropriate protective gear such as mouthguards, hand wraps, gloves, shin guards, or headgear. This helps minimize the risk of injuries to vulnerable areas of the body.</strong></li>
                <li><span style="color:red;"><strong>Safety equipment and training environment:</span> Ensure that your training environment is safe and well-maintained. Avoid training on uneven or slippery surfaces, and remove any potential hazards from the training area. Use proper training equipment, such as mats or padding, when necessary.</strong></li>
                <li><span style="color:red;"><strong>Warm-down and recovery:</span> After each training session, engage in a cool-down routine to gradually lower your heart rate and stretch your muscles. This promotes recovery and reduces post-training muscle soreness.</strong></li>
                <li><span style="color:red;"><strong>Listen to your body:</span> Pay attention to any pain or discomfort during training. If you experience unusual pain, dizziness, or difficulty breathing, stop training and seek medical attention if necessary. Pushing through severe pain can lead to further injury.</strong></li>
                <li><span style="color:red;"><strong>Cross-training and rest:</span> Avoid overtraining by incorporating rest days into your training schedule. Cross-train in other forms of exercise to promote overall fitness and prevent overuse injuries.</strong></li>
                <li><span style="color:red;"><strong>Communication with instructors:</span> Communicate openly with your instructors about any health conditions, injuries, or concerns you may have. They can provide guidance, modifications, or adjustments to your training to accommodate your needs and ensure your safety.</strong></li>
                <li><span style="color:red;"><strong>Respect for training partners:</span> Show respect and consideration for your training partners during sparring or partner drills. Follow rules and guidelines, and avoid using excessive force. Practicing control and good sportsmanship helps create a safe training environment for everyone involved.</strong></li>
            </ol>
            """,
            unsafe_allow_html=True
        )

    @Rule(IndividualSportsType(individualSports_type='Archery'))
    def Archery(self):
        st.markdown("""<h3 style="text-align: center;">Archery</h3>""", unsafe_allow_html=True)
        image = Image.open('images/images_sport/archery.jpg')
        st.image(image, use_column_width=True)

        st.markdown(
            """
            <strong style="text-style: bold; font-size: 20px;">Archery is an ancient art and sport that involves using a bow to shoot arrows at a target. The bow is a flexible piece of equipment with a string attached between two limbs. Arrows are propelled by pulling back and releasing the bowstring, which transfers energy to the arrow and propels it towards the target.  It combines precision, focus, and technique to achieve accuracy and consistency in hitting the target. Archery has evolved from its historical origins as a hunting and warfare skill into a popular recreational and competitive activity.</strong>
            <br/><br/>
            <span style="font-size:20px;"><strong>Advantages of Archery:</strong></span>
            <ol>
                <li><span style="color:blue;"><strong>Focus and concentration:</span> Archery requires mental focus and concentration. Shooters must block out distractions and maintain focus on the target, aiming for precision and accuracy. It promotes mindfulness and helps develop mental discipline.</strong></li>
                <li><span style="color:blue;"><strong>Physical coordination and strength:</span> Archery engages various muscle groups in the arms, shoulders, back, and core. Drawing the bowstring requires strength, control, and coordination. Regular practice can improve upper body strength, stability, and overall physical fitness.</strong></li>
                <li><span style="color:blue;"><strong>Precision and accuracy:</span> Archery is a discipline that demands precision. Shooters strive to consistently hit the target's center or specific scoring zones. It requires fine motor skills, hand-eye coordination, and control over breathing and body posture.</strong></li>
                <li><span style="color:blue;"><strong>Patience and discipline:</span> Archery cultivates patience and discipline. It teaches shooters to take their time, follow a consistent shooting routine, and remain focused even during long periods of practice. It promotes mental fortitude and the ability to manage pressure.</strong></li>
                <li><span style="color:blue;"><strong>Stress relief and relaxation:</span> The repetitive and focused nature of archery can have a calming effect, providing stress relief and promoting relaxation. The rhythmic process of shooting arrows can help clear the mind and provide a sense of tranquility.</strong></li>
                <li><span style="color:blue;"><strong>Social and competitive engagement:</span> Archery can be enjoyed as a solitary activity or as a social and competitive sport. Participating in archery clubs, events, or competitions allows for interaction with other archers, fostering a sense of community, camaraderie, and healthy competition.</strong></li>
                <li><span style="color:blue;"><strong>Outdoor connection:</span> Archery can be practiced both indoors and outdoors, offering opportunities to connect with nature. Outdoor archery ranges provide a scenic backdrop, allowing archers to enjoy fresh air and natural surroundings while honing their skills.</strong></li>
            </ol>
            <br/>
            <span style="font-size:20px;"><strong>Precautions of Archery:</strong></span>
            <ol>
                <li><span style="color:red;"><strong>Safety protocols:</span> Adhere to safety guidelines and rules set by the archery range or facility. Ensure a safe shooting environment, follow proper range etiquette, and use safety equipment such as arm guards and finger tabs or gloves.</strong></li>
                <li><span style="color:red;"><strong>Proper form and technique:</span> Learn and practice proper shooting form and technique under the guidance of a qualified instructor. This helps prevent injuries and ensures optimal performance.</strong></li>
                <li><span style="color:red;"><strong>Equipment maintenance:</span> Regularly inspect and maintain your archery equipment, including the bow, arrows, and string. Keep the equipment in good condition to ensure safe and reliable performance.</strong></li>
                <li><span style="color:red;"><strong>Knowledge of range rules:</span> Familiarize yourself with the rules and regulations specific to the archery range or facility you are using. Observe range protocols and respect the instructions provided by range officials.</strong></li>
            </ol>
            """,
            unsafe_allow_html=True
        )

    @Rule(IndividualSportsType(individualSports_type='Skiing'))
    def Skiing(self):
        st.markdown("""<h3 style="text-align: center;">Skiing</h3>""", unsafe_allow_html=True)
        image = Image.open('images/images_sport/skiing.jpg')
        st.image(image, use_column_width=True)

        st.markdown(
            """
            <strong style="text-style: bold; font-size: 20px;">Skiing involves strapping skis to your feet and using poles for balance and propulsion. Skis have a smooth base that allows for gliding over the snow, and bindings that securely attach boots to the skis. It combines physical exertion, technical skill, and a connection with nature.</strong>
            <br/><br/>
            <span style="font-size:20px;"><strong>Advantages of Skiing:</strong></span>
            <ol>
                <li><span style="color:blue;"><strong>Outdoor adventure:</span> Skiing takes place in beautiful winter landscapes, providing an opportunity to connect with nature and enjoy the outdoors. Skiers can experience breathtaking mountain views, fresh air, and the tranquility of snowy surroundings.</strong></li>
                <li><span style="color:blue;"><strong>Physical fitness:</span> Skiing is a physically demanding activity that engages the entire body. It requires leg strength, balance, and core stability to navigate slopes and maintain control. Skiing also provides a cardiovascular workout, improving endurance and overall fitness.</strong></li>
                <li><span style="color:blue;"><strong>Thrill and excitement:</span> Skiing offers a sense of speed, adrenaline, and excitement. Carving turns down a mountain or gliding through powder snow can provide an exhilarating sensation. Skiing can be tailored to individual preferences, with options for both relaxed cruising and more challenging descents.</strong></li>
                <li><span style="color:blue;"><strong>Skill development:</span> Skiing involves learning and refining specific techniques, such as turning, edging, and balancing. It requires coordination, timing, and body control. As skiers progress, they can challenge themselves with steeper slopes, moguls, or terrain parks, continually improving their skills.</strong></li>
                <li><span style="color:blue;"><strong>Winter tourism and vacation:</span> Skiing is a significant part of winter tourism in many regions. Ski resorts offer a range of amenities, including accommodation, dining, and après-ski activities. Ski trips provide opportunities for relaxation, entertainment, and exploration of winter destinations.</strong></li>
            </ol>
            <br/>
            <span style="font-size:20px;"><strong>Precautions of Skiing:</strong></span>
            <ol>
                <li><span style="color:red;"><strong>Safety awareness:</span> Prioritize safety by following resort guidelines, slope rules, and any posted signs. Be aware of your surroundings, ski within your abilities, and respect the mountain environment.</strong></li>
                <li><span style="color:red;"><strong>Proper equipment and gear:</span>  Ensure that your ski equipment, including skis, bindings, boots, and poles, is properly maintained and adjusted to your specifications. Wear appropriate clothing and protective gear, including helmets, goggles, and layers to stay warm and comfortable.</strong></li>
                <li><span style="color:red;"><strong>Ski lessons and skill development:</span> Take ski lessons, especially if you're a beginner or looking to improve your technique. Learning from certified instructors can enhance safety, skill development, and overall enjoyment.</strong></li>
                <li><span style="color:red;"><strong>Avalanche and off-piste awareness:</span> If venturing into backcountry or off-piste areas, obtain proper avalanche safety training and knowledge. Understand the risks associated with skiing in uncontrolled environments and carry necessary safety equipment, such as avalanche transceivers, shovels, and probes.</strong></li>
                <li><span style="color:red;"><strong>Hydration and sun protection:</span> Stay hydrated by drinking plenty of water, as skiing can be physically demanding. Protect yourself from the sun's harmful rays by wearing sunscreen, lip balm, and appropriate eyewear.</strong></li>
                <li><span style="color:red;"><strong>Weather conditions and visibility:</span> Be aware of changing weather conditions and their impact on slope conditions and visibility. Adjust your skiing plans accordingly and ski with caution during adverse weather, such as heavy snowfall or reduced visibility.</strong></li>
            </ol>
            """,
            unsafe_allow_html=True
        )
                
    @Rule(IndividualSportsType(individualSports_type='Diving'))
    def Diving(self):
        st.markdown("""<h3 style="text-align: center;">Diving</h3>""", unsafe_allow_html=True)
        image = Image.open('images/images_sport/diving.jpg')
        st.image(image, use_column_width=True)

        st.markdown(
            """
            <strong style="text-style: bold; font-size: 20px;">Diving offers a unique opportunity to explore the underwater world, filled with vibrant marine life, coral reefs, and fascinating geological formations. Whether diving in tropical waters or exploring shipwrecks, divers immerse themselves in a captivating environment that is inaccessible to most.</strong>
            <br/><br/>
            <span style="font-size:20px;"><strong>Advantages of Diving:</strong></span>
            <ol>
                <li><span style="color:blue;"><strong>Exploration and adventure:</span> Diving allows individuals to venture into a world that is vastly different from the terrestrial environment. It offers the thrill of discovering new underwater landscapes, encountering marine creatures, and uncovering hidden treasures.</strong></li>
                <li><span style="color:blue;"><strong>Appreciation of marine life:</span> Divers have the chance to witness the diverse marine ecosystem up close. They can observe colorful fish, coral reefs, sea turtles, dolphins, and other fascinating aquatic creatures in their natural habitats. Diving fosters an understanding of the importance of marine conservation and promotes a sense of responsibility towards protecting the underwater environment.</strong></li>
                <li><span style="color:blue;"><strong>Sense of tranquility:</span> Being underwater can provide a sense of tranquility and serenity. The weightlessness, silence, and gentle movements of diving create a peaceful and meditative experience, allowing divers to escape from the hustle and bustle of the surface world.</strong></li>
                <li><span style="color:blue;"><strong>Physical fitness:</span> Diving is a physically demanding activity that engages multiple muscle groups. It improves cardiovascular endurance, strength, flexibility, and coordination. The resistance provided by water adds an additional challenge to movements, making diving an effective form of low-impact exercise.</strong></li>
                <li><span style="color:blue;"><strong>Mental focus and mindfulness:</span> Diving requires concentration, mental focus, and awareness of one's surroundings. It encourages divers to be present in the moment and fully engaged in their underwater experience. The calm and serene underwater environment can have a relaxing and rejuvenating effect on the mind.</strong></li>
                <li><span style="color:blue;"><strong>Social and community connections:</span> Diving is often enjoyed as a social activity, providing opportunities to connect with fellow divers, share experiences, and build lasting friendships. Diving clubs, group trips, and training courses foster a sense of camaraderie and community among diving enthusiasts.</strong></li>
            </ol>
            <br/>
            <span style="font-size:20px;"><strong>Precautions of Diving:</strong></span>
            <ol>
                <li><span style="color:red;"><strong>Training and certification:</span> Obtain proper training and certification from recognized diving organizations. Learn essential skills, safety procedures, and diving techniques from qualified instructors to ensure safe and responsible diving practices.</strong></li>
                <li><span style="color:red;"><strong>Equipment checks:</span> Regularly inspect and maintain your diving equipment, including the scuba tank, regulator, buoyancy control device(BCD), and other gear. Ensure proper functioning and seek professional assistance if any issues arise.</strong></li>
                <li><span style="color:red;"><strong>Dive planning and safety procedures:</span> Plan dives within your training and experience level. Consider factors such as depth, currents, visibility, and dive duration. Follow proper safety procedures, including buddy diving, pre-dive checks, and adherence to decompression limits.</strong></li>
                <li><span style="color:red;"><strong>Underwater communication:</span> Learn and utilize proper underwater communication techniques, such as hand signals, to communicate effectively with your dive partner or group. Clear communication enhances safety and ensures a shared understanding during the dive.</strong></li>
                <li><span style="color:red;"><strong>Equalization and ascent rates:</span> Properly equalize your ears and sinuses to relieve pressure changes during descent. Ascend slowly and maintain proper ascent rates to minimize the risk of decompression sickness.</strong></li>
                <li><span style="color:red;"><strong>Environmental awareness:</span> Respect the underwater environment and follow responsible diving practices. Avoid touching or damaging marine life, refrain from littering, and adhere to local regulations and conservation efforts./strong></li>
            </ol>
            """,
            unsafe_allow_html=True
        )
    
        
    
        
        
        
        