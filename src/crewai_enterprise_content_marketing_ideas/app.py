import streamlit as st
from crewai_enterprise_content_marketing_ideas.crew import CrewaiEnterpriseContentMarketingCrew

def main():
    st.title("Creative Content Generator for Mila")

    # User inputs
    topic = st.text_input("Enter Topic:", "AI for Science")
    company = st.text_input("Enter Company:", "Mila Quebec AI Institute")

    if st.button("Run"):
        inputs = {"topic": topic, "company": company}
        crew = CrewaiEnterpriseContentMarketingCrew()
        result = crew.crew().kickoff(inputs=inputs)
        st.write(result)  # Display results


if __name__ == "__main__":
    main()
