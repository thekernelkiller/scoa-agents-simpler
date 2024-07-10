from crewai import Agent
from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv
load_dotenv()


llm = ChatGoogleGenerativeAI(model= "gemini-1.5-flash", temperature=0.3, top_p= 0.7)

class SCOAAgents:
    def sc_analyst_agent(self):
        return Agent(
            role = "The best strengths and challenges analyser",
            goal = "Provide our user the best strengths and challenges report based on their responses and benchmark data.",
            backstory = "Known as the best student performance analyser, you're skilled in identifying the core strengths and challenges of a student by analysing their responses based on the years of experience you have.",
            llm = llm,
            max_iter = 9,
            allow_delegation = True,
            verbose = True

        )
    
    def oa_analyst_agent(self):
        return Agent(
            role = "The best opportunities and actionables generator",
            goal = "Provide our user the best opportunities and actionables report based on their strengths and challenges report.",
            backstory = "Known as the best student mentor, you're skilled in identifying a student's opportunities and can prepare the best set of actions to improve their performance, based on their strengths and challenges report.",
            llm = llm,
            max_iter = 9,
            allow_delegation = True,
            verbose = True,

        )
    
    def manager_agent(self):
        return Agent(
            role = "Manager",
            goal = "Manage the crew and ensure the opportunities and actionables report is based on strengths and challenges.",
            backstory = "Known as the best manager, you're experienced in overseeing complex projects and guiding teams to success. Your role is to coordinate the efforts of the crew members, ensuring that each task is completed on time and to the highest standard.",
            llm = llm,
            max_iter = 9,
            allow_delegation = False,
            verbose = True

        )