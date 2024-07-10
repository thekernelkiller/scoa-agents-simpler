import os
from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma

from dotenv import load_dotenv
load_dotenv()

def create_embeddings(urls):
    # Load web pages
    loader = WebBaseLoader(urls)
    documents = loader.load()

    # Split text into chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    splits = text_splitter.split_documents(documents)

    # Create embeddings and store in ChromaDB
    embedding_function = OpenAIEmbeddings()
    vectorstore = Chroma.from_documents(
        documents=splits,
        embedding=embedding_function,
        persist_directory="./chroma_db"
    )

    # Persist the database
    vectorstore.persist()
    print(f"Embeddings created and stored for {len(urls)} URLs.")

if __name__ == "__main__":
    # Example usage
    websites = [
    "https://www.allen.ac.in/engineering/jee-main/tips-tricks/",
    "https://motion.ac.in/blog/jee-main-weightage-chapter-wise/",
    "https://www.allen.ac.in/engineering/jee-main/preparation-strategy/",
    "https://byjus.com/jee/how-to-prepare-for-jee-at-home/",
    "https://www.askiitians.com/iit-jee/how-to-prepare-for-iit-jee-from-class-11.html",
    "https://byjus.com/jee/complete-study-plan-to-crack-jee-main/",
    "https://www.allenoverseas.com/blog/jee-main-2024-exam-strategies-subject-wise-preparation-tips/",
    "https://www.vedantu.com/jee-main/topics",
    "https://www.pw.live/exams/wp-content/uploads/2024/01/syllabus-for-jee-main-2024-as-on-01-november-2023-1-3.pdf",
    "https://www.pw.live/exams/wp-content/uploads/2024/01/syllabus-for-jee-main-2024-as-on-01-november-2023-4-8.pdf",
    "https://www.pw.live/exams/jee/jee-main-chemistry-syllabus/",
    "https://www.pw.live/topics-chemistry-class-11",
    "https://www.pw.live/topics-chemistry-class-12"
]
    create_embeddings(websites)



# ---
# from dotenv import load_dotenv
# from embedchain import App
# load_dotenv()

# urls = [
#     "https://www.allen.ac.in/engineering/jee-main/tips-tricks/",
#     "https://motion.ac.in/blog/jee-main-weightage-chapter-wise/",
#     "https://www.allen.ac.in/engineering/jee-main/preparation-strategy/",
#     "https://byjus.com/jee/how-to-prepare-for-jee-at-home/",
#     "https://www.askiitians.com/iit-jee/how-to-prepare-for-iit-jee-from-class-11.html",
#     "https://byjus.com/jee/complete-study-plan-to-crack-jee-main/",
#     "https://www.allenoverseas.com/blog/jee-main-2024-exam-strategies-subject-wise-preparation-tips/",
#     "https://www.vedantu.com/jee-main/topics",
#     "https://www.pw.live/exams/wp-content/uploads/2024/01/syllabus-for-jee-main-2024-as-on-01-november-2023-1-3.pdf",
#     "https://www.pw.live/exams/wp-content/uploads/2024/01/syllabus-for-jee-main-2024-as-on-01-november-2023-4-8.pdf",
#     "https://www.pw.live/exams/jee/jee-main-chemistry-syllabus/",
#     "https://www.pw.live/topics-chemistry-class-11",
#     "https://www.pw.live/topics-chemistry-class-12"
# ]

# app = App.from_config(config_path="config.yaml")
# #     config={
# #         "app": {
# #             "config": {
# #                 "id": "jee-roadmap-app"
# #             }
# #         },
# #         "embedder": {
# #             "provider": "gpt4all"
# #         }
# #     }
# # )

# for url in urls:
#     app.add(url)
#     print(f"Added and embedded: {url}")

# print("Embedding and data storage complete!")