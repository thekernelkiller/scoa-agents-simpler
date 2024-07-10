# from langchain_community.vectorstores import Chroma
# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain.chains import RetrievalQAWithSourcesChain
# from langchain.prompts import PromptTemplate
# from langchain.tools import Tool

# class RAGTool:
#     vectorstore = None
#     qa_chain = None

#     @classmethod
#     def initialize(cls):
#         if cls.vectorstore is None:
#             # Load the persisted Chroma database
#             cls.vectorstore = Chroma(persist_directory="./chroma_db")

#             # Initialize the language model (using Google's Generative AI as in your agents.py)
#             llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.3)

#             # Create a custom prompt template
#             prompt_template = """
#             You are an AI assistant helping with JEE (Joint Entrance Examination) performance analysis.
#             Use the following pieces of context to answer the question at the end.
#             If you don't know the answer, just say that you don't know, don't try to make up an answer.
#             Always include the sources of your information in your answer.

#             Context: {summaries}

#             Question: {question}

#             Answer: """

#             PROMPT = PromptTemplate(
#                 template=prompt_template,
#                 input_variables=["summaries", "question"]
#             )

#             # Create a retrieval chain with sources
#             cls.qa_chain = RetrievalQAWithSourcesChain.from_chain_type(
#                 llm=llm,
#                 chain_type="stuff",
#                 retriever=cls.vectorstore.as_retriever(),
#                 chain_type_kwargs={"prompt": PROMPT}
#             )

#     @classmethod
#     def query(cls, question: str) -> str:
#         """Query the RAG system with a question about JEE."""
#         cls.initialize()
#         result = cls.qa_chain({"question": question})
#         answer = result['answer']
#         sources = result['sources']
#         return f"Answer: {answer}\n\nSources: {sources}"

# def get_rag_tool():
#     """A Tool for the RAG system."""
#     return Tool(
#         name="JEE Information Retrieval",
#         func=RAGTool.query,
#         description="Use this tool to get information about JEE preparation, topics, strategies, and benchmark data. Input should be a specific question related to JEE."
#     )

# # Initialize the RAGTool
# RAGTool.initialize()


# from langchain_community.vectorstores import Chroma
# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain.chains import RetrievalQAWithSourcesChain
# from langchain.prompts import PromptTemplate
# from langchain.tools import tool


# class RAGTool:
#     vectorstore = None
#     qa_chain = None

#     @classmethod
#     def initialize(cls):
#         if cls.vectorstore is None:
#             # Load the persisted Chroma database
#             cls.vectorstore = Chroma(persist_directory="./chroma_db")

#             # Initialize the language model
#             llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

#             # Create a custom prompt template
#             prompt_template = """
#             You are an AI assistant helping with student performance analysis.
#             Use the following pieces of context to answer the question at the end.
#             If you don't know the answer, just say that you don't know, don't try to make up an answer.
#             Always include the sources of your information in your answer.

#             Context: {summaries}

#             Question: {question}

#             Answer: """

#             PROMPT = PromptTemplate(
#                 template=prompt_template,
#                 input_variables=["summaries", "question"]
#             )

#             # Create a retrieval chain with sources
#             cls.qa_chain = RetrievalQAWithSourcesChain.from_chain_type(
#                 llm=llm,
#                 chain_type="stuff",
#                 retriever=cls.vectorstore.as_retriever(),
#                 chain_type_kwargs={"prompt": PROMPT}
#             )

#     @tool
#     def query_rag(question: str) -> str:
#         """Use this tool to get information about student performance analysis, study techniques, and educational strategies. 
#         Input should be a specific question related to academic performance, study habits, or cognitive aspects of learning."""
#         RAGTool.initialize()
#         result = RAGTool.qa_chain({"question": question})
#         answer = result['answer']
#         sources = result['sources']
#         return f"Answer: {answer}\n\nSources: {sources}"

# # Initialize the RAGTool
# RAGTool.initialize()

# # The tool can be accessed as RAGTool.query_rag

# if __name__ == "__main__":
#     # Example usage
#     result = RAGTool.query_rag("What are effective study techniques for improving problem-solving skills in mathematics?")
#     print(result)



# ---
# from embedchain import App
# from langchain.tools import Tool

# class RAGTool():
#     def __init__(self):
#         self.app = App.from_config(config_path="config.yaml")

#     def search_internet(self, query: str) -> str:
#         """Searches the JEE context information and returns relevant results."""
#         result = self.app.query(query)  
#         return result

#     @property
#     def rag_tool(self):
#         return Tool(
#             name="Search the internet",
#             func=self.search_internet,
#             description="Searches the JEE context information and returns relevant results."
        # )


# ---
# from crewai_tools import DirectoryReadTool

# # # Initialize the tool so the agent can read any directory's content it learns about during execution
# RAGTool = DirectoryReadTool(directory='chroma_db')

# OR

# Initialize the tool with a specific directory, so the agent can only read the content of the specified directory
#tool = DirectoryReadTool(directory='db')