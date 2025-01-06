import streamlit as st
import sys

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

