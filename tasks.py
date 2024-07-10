from crewai import Task
from textwrap import dedent

class SCOATasks:
    def sc_analysis_task(self, sc_analyst_agent, math_confidence, physics_confidence, chemistry_confidence, study_question, cognitive_question):
        return Task(
            description = dedent(f"""
                Analyse and find the student's strengths and challenges based on their JEE preparation confidence scores, study profile and cognitive questionnaire responses.

                Your response should be structured in the following format:

                **Strengths**:
                - [Strength 1 description - based on physics]
                - [Strength 2 description - based on chemistry] 
                - [Strength 3 description - based on maths]
                - [Strength 4 description - based on study profile]
                - [Strength 5 description - based on cognitive profile] 
                
                **Challenges**:
                - [Challenge 1 description - based on physics]
                - [Challenge 2 description - based on chemistry] 
                - [Challenge 3 description - based on maths]
                - [Challenge 4 description - based on study profile]
                - [Challenge 5 description - based on cognitive profile] 
                                 
                Inputs:
                {math_confidence}, {physics_confidence}, {chemistry_confidence}, {study_question}, {cognitive_question}
                
            """),
            agent = sc_analyst_agent,
            # async_execution = True,
            expected_output = dedent(f"""
                **Strengths**:
                    1. **Physics:** You demonstrate strong understanding in Modern Physics, Thermodynamics, Waves and Fluid Mechanics, and Electromagnetism, reflected in your high confidence scores. This indicates a strong foundation in these areas and a potential for you to score big in these topics if practiced well.
                    2. **Chemistry:** You excel in Physical Chemistry, both 11th and 12th grade topics. Practise difficult and more variety of questions from these topics to score big in the exam.
                    3. **Mathematics:** You show strength in Differential Calculus, Sets, Relations and Functions, and Trigonometry, indicating a good understanding of these core mathematical concepts. Although you need to practise many problems to apply your theortical knowledge in the exam.
                    4. **Study Behaviour:** You utilize calendars and to-do apps to monitor progress, indicating an organized approach to learning and tracking your performance. Keep it up!
                    5. **Cognitive Feature:** You are highly likely to identify and resolve misconceptions, demonstrating a willingness to learn from mistakes and improve their understanding. Amazing!
                                     
                **Challenges**:
                    1. **Physics:**  Your confidence scores in Mechanics (3), Electricity and Electrostatics (5) is significantly lower than other topics. This indicates a potential weakness in foundational concepts related to motion, forces, and Newton's laws. Revise or Learn these concepts again and start by practising basic problems.
                    2. **Chemistry:** Your confidence scores in 11th Organic Chemistry (4)  and 12th Organic Chemistry indicate significant difficulty in this area. This might be due to a lack of understanding of basic organic chemistry concepts like nomenclature, functional groups, and reaction mechanisms. Learn these concepts as they are rank deciders in JEE.
                    3. **Mathematics:** Your confidence score in Coordinate Geometry (6) indicates a potential challenge in visualising and applying in complex geometric problems. Start practising more problems in increasing difficulty.
                    4. **Study Behaviour:** While you claim to revise frequently, the low confidence scores in certain topics suggest a lack of deep understanding or difficulty in retaining concepts for the long term.  Explore different learning methods like mind mapping and spaced repetition to improve retention.
                    5. **Cognitive Feature:** Your cognitive response regarding time management indicates a potential issue. Consistently running late during exams could lead to stress and negatively impact performance. Implement time management strategies during practice sessions and mock tests.
            """)
        )
    
    def oa_analysis_task(self, oa_agent, context):
        return Task(
            description = dedent(f"""
                Based on the strengths and challenges report, identify the potential opportunities the student has.
                Design high quality and insightful actionables the student can incorporate.

                Structure your response as follows:

                **Opportunities**:
                - [Opportunity 1 description - based on physics]
                - [Opportunity 2 description - based on chemistry] 
                - [Opportunity 3 description - based on maths]
                - [Opportunity 4 description - based on study profile]
                - [Opportunity 5 description - based on cognitive profile] 
                
                **Actionables**: 
                - [Actionable 1 description - based on physics]
                - [Actionable 2 description - based on chemistry] 
                - [Actionable 3 description - based on maths]
                - [Actionable 4 description - based on study profile]
                - [Actionable 5 description - based on cognitive profile] 
                
                Maintain a friendly and progressive tone throughout. Address the student directly using "you" and "your".
                {SCOAHelpers.bonus_section()}
            """),
            agent = oa_agent,
            # async_execution = True,
            context = context,
            expected_output = dedent(f"""
                **Opportunities**:
                    1. **Physics:** Your score of 6 in Waves and Fluid Mechanics indicate a good understanding but with room for improvement. This topic has a moderate weightage in JEE. Practice more challenging problems, focus on understanding the underlying principles, and try to connect the concepts to real-life scenarios.
                    2. **Chemistry:** Your score of 6 in Inorganic Chemistry indicates a good understanding but with room for improvement. Inorganic chemistry has a significant weightage in JEE. 
                    3. **Mathematics:** Your score of 6 in Coordinate Geometry indicates a good understanding but with room for improvement. Coordinate geometry is a crucial topic with good weightage in JEE. Practise more challenging problems. For better understanding watch tutorials that visualise concepts. Revise NCERT text-book frequently and focus on understanding the periodic trends and properties of elements. Use mind maps or flowcharts to organize the information.
                    4. **Study Behaviour:** You mentioned allocating your time almost equally for Physics, Chemistry, and Mathematics. Consider a more dynamic approach based on your individual strengths and weaknesses. Allocate more time to topics where you have lower confidence scores and higher weightage in the syllabus.
                    5. **Cognitive Feature:** You mentioned integrating feedback "sometimes". Actively seek feedback, analyze your mistakes, and modify your study plan accordingly. Focus on areas where you need improvement. By discussing with your faculties and friends, you can retain concepts strongly.
                                     
                **Actionables**: 
                    1. Follow a detailed study plan that includes specific goals for each topic and chapter. Track your progress using our Sstudize app which provides extensive progress tracking features!
                    2. Identify the root cause of your difficulty. Is it a lack of understanding of fundamental concepts, or are you struggling with specific problem-solving techniques? Tailor your approach accordingly. For example, if you struggle with a concept, revisit the theory, watch video explanations, and seek help from your coaching faculty.
                    3. Practice time-bound mock tests to simulate exam conditions. Analyze your performance and identify areas where you need to improve your speed and accuracy. Consider using strategies like working through easier questions first and allocating time wisely for each section.
                    4. Develop a system for reviewing your notes and practice problems to identify areas where you may have made errors or formed incorrect assumptions. Seek clarification from coaching tutor if necessary.
                    5. Always be confident and positive about your preparation journey! Remember: the journey is just as much important as the result. Be true to yourself and consistent in your preparation. You got this!

            """)
        )
    

class SCOAHelpers:
    @staticmethod
    def bonus_section():
        return "If you do your BEST WORK, I'll give you a bonus of ₹10000!"
    
    # @staticmethod
    # def format_scores(scores):
    #     return "\n".join([f"- {topic}: {score}" for topic, score in scores.items()])
    
    # @staticmethod
    # def format_qa_pairs(qa_dict):
    #     formatted_pairs = []
    #     for key, value in qa_dict.items():
    #         question = SCOAHelpers.get_question(key)
    #         formatted_pairs.append(f"Q: {question}\nA: {value}")
    #     return "\n\n".join(formatted_pairs)
    
    # @staticmethod
    # def get_question(key):
    #     questions = {
    #         'time_division': "How do you divide your study time among Physics, Chemistry and Mathematics for JEE? (Allocate Percentage)",
    #         'mock_test_frequency': "How often do you use mock tests and past question papers for JEE preparation?",
    #         'progress_monitoring': "How do you monitor your progress in JEE topics or chapters?",
    #         'study_methods': "How do you adjust your study methods for difficult or new JEE topics?",
    #         'study_techniques': "What techniques do you use to remember JEE concepts and formulas for a long time? eg: Revise frequently, Mindmap, etc.",
    #         'problem_solving_approach': "When faced with complex, multi-step problems in JEE, how likely are you to approach problem-solving systematically, breaking down each step?",
    #         'thorough_understanding': "In your JEE preparation, how likely are you to ensure thorough understanding of fundamental concepts before moving on to advanced topics?",
    #         'feedback': "How likely are you to integrate feedback from practice tests or teachers into your JEE preparation strategy?",
    #         'misconception': "When encountering a misconception or misunderstanding in a JEE concept, how likely are you to identify and resolve it?",
    #         'time_management': "How likely are you to effectively manage time during JEE exams, especially in sections with limited time constraints?"
    #     }
    #     return questions.get(key, "Question not found")