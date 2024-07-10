from crewai import Agent, Task, Crew, Process
from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_openai import ChatOpenAI
from textwrap import dedent
from agents import SCOAAgents
from tasks import SCOATasks

from dotenv import load_dotenv
load_dotenv()

class SCOACrew:
    def __init__(self, math_confidence, physics_confidence ,chemistry_confidence, study_question, cognitive_question):
        self.math_confidence = math_confidence
        self.physics_confidence = physics_confidence
        self.physics_confidence = chemistry_confidence
        self.study_question = study_question
        self.cognitive_question = cognitive_question

    def run(self):
        agents = SCOAAgents()
        tasks = SCOATasks()

        sc_analyst_agent = agents.sc_analyst_agent()
        oa_analyst_agent = agents.oa_analyst_agent()
        manager_agent = agents.manager_agent()

        sc_analysis_task = tasks.sc_analysis_task(
            sc_analyst_agent,
            self.math_confidence,
            self.physics_confidence,
            self.physics_confidence,
            self.study_question,
            self.cognitive_question
        )

        oa_analysis_task = tasks.oa_analysis_task(
            oa_analyst_agent,
            [sc_analysis_task]
        )

        crew = Crew(
            agents = [sc_analyst_agent, oa_analyst_agent],
            tasks = [sc_analysis_task, oa_analysis_task],
            manager_agent = manager_agent,
            process = Process.hierarchical,
            manager_llm= ChatGoogleGenerativeAI(model = "gemini-1.5-flash", temperature=0.3, top_p= 0.7),
            # manager_llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.3, max_tokens=2000),
            verbose = True
        )

        result = crew.kickoff()
        print(result)
    

if __name__ == "__main__":
    print("## Welcome to SCOA Analyser!")
    print('-------------------------------')


    # academic_scores = {
    #     'maths': {},
    #     'physics': {},
    #     'chemistry': {}
    # }

    math_confidence = input(dedent(f"Rate your confidence in math (1-10): "))
    physics_confidence = input(dedent(f"Rate your confidence in physics (1-10): "))
    chemistry_confidence = input(dedent(f"Rate your confidence in chemistry (1-10): "))
    study_question = input(dedent(f"How do you adjust your study methods for difficult or new JEE topics?: "))
    cognitive_question = input(dedent(f"How likely are you to integrate feedback from practice tests or teachers into your JEE preparation strategy?: "))

    # study_profile = {}
    # cognitive_inputs = {}
    

    # physics_topics = [
    #     "Kinematics", "Mechanics", "Waves and Fluid Mechanics", "Thermodynamics",
    #     "Electricity and Electrostatics", "Electromagnetism", "Optics", "Modern Physics"
    # ]

    # chemistry_topics = [
    #     "11th Physical Chemistry", "11th Inorganic Chemistry", "11th Organic Chemistry",
    #     "12th Physical Chemistry", "12th Inorganic Chemistry", "12th Organic Chemistry"
    # ]

    # maths_topics = [
    #     "Sets, Relations and Functions", "Algebra", "Trigonometry", "Coordinate Geometry",
    #     "Differential Calculus", "Integral Calculus", "Vector Algebra and 3D Geometry",
    #     "Statistics and Probability"
    # ]

    # study_profile_prompts = {
    #     'time_division': "How do you divide your study time among Physics, Chemistry and Mathematics for JEE ? (Allocate Percentage)",
    #     'mock_test_frequency': "How often do you use mock tests and past question papers for JEE preparation ?",
    #     'progress_monitoring': "How do you monitor your progress in JEE topics or chapters",
    #     'study_methods': "How do you adjust your study methods for difficult or new JEE topics ?",
    #     'study_techniques': "What techniques do you use to remember JEE concepts and formulas for a long time ? eg: Revise frequently, Mindmap, etc."
    # }

    # cognitive_inputs_prompts = {
    #     'problem_solving_approach': "When faced with complex,multi-stemp problems in JEE, how likely are you to approach problem-solving systematically, breaking down each step ?",
    #     'thorough_understanding': "In your JEE preparation, how likely are you to ensure thorough understanding of fundamental concepts before moving on to advanced topics ?",
    #     'feedback': "How likely are you to integrate feedback from practice tests or teachers into your JEE preparation strategy ?",
    #     'misconception': "When encountering a misconception or misunderstanding in a JEE concept, how likely are you to identify and resolve it ?",
    #     'time_management': "How likely are you to effectively manage time during JEE exams, especially in sections with limited time constraints?"
    # }



    # # Collect confidence scores for each subject
    # print("\nEnter your confidence scores for Physics topics:")
    # for topic in physics_topics:
    #     academic_scores['physics'][topic] = input(dedent(f"Rate your confidence in {topic} (1-10): "))

    # print("\nEnter your confidence scores for Chemistry topics:")
    # for topic in chemistry_topics:
    #     academic_scores['chemistry'][topic] = input(dedent(f"Rate your confidence in {topic} (1-10): "))

    # print("\nEnter your confidence scores for Maths topics:")
    # for topic in maths_topics:
    #     academic_scores['maths'][topic] = input(dedent(f"Rate your confidence in {topic} (1-10): "))

    # print("\nAnswer the following study profile questions:")
    # for key, prompt in study_profile_prompts.items():
    #     study_profile[key] = input(dedent(prompt))

    # print("\nAnswer the following cognitive questions:")
    # for key, prompt in cognitive_inputs_prompts.items():
    #     cognitive_inputs[key] = input(dedent(prompt))


    # Create an instance of SCOACrew and run the process
    scoa_crew = SCOACrew(math_confidence, physics_confidence ,chemistry_confidence, study_question, cognitive_question)
    result = scoa_crew.run()
    print(result)


