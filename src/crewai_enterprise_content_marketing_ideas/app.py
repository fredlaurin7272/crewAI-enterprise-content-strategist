import streamlit as st
import sys
import sqlite3


import chromadb
client = chromadb.Client()
collection = client.get_collection(name="chroma_docs")
results = collection.get(ids=["page"])["documents"]
print(results) # Not found []


# # Specify the path to your module
# module_path = "C:/Users/Frederic Laurin/PycharmProjects/crewAI-enterprise-content-marketing-ideas-template-main/src"

# # Check if the path is already in sys.path
# if module_path not in sys.path:
#     sys.path.append(module_path)  # Add the path to sys.path

# # Verify if the path was added (optional)
# print(module_path in sys.path)  # This should print True if added successfully

from crewai_enterprise_content_marketing_ideas.crew import CrewaiEnterpriseContentMarketingCrew

st.title("Creative Content Generator for Mila")

# User inputs
topic = st.text_input("Enter Topic:", "AI for Science")
company = st.text_input("Enter Company:", "Mila Quebec AI Institute")

if st.button("Run"):
    inputs = {"topic": topic, "company": company}
    crew = CrewaiEnterpriseContentMarketingCrew()
    result = crew.crew().kickoff(inputs=inputs)
    st.write(result.raw)  # Display results

