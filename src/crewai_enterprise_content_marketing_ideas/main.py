#!/usr/bin/env python
import pysqlite3 as sqlite3
__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

import sys
from crewai_enterprise_content_marketing_ideas.crew import (
    CrewaiEnterpriseContentMarketingCrew,
)


def run():
    """
    Run the crew.
    """
    inputs = {"topic": "AI for Science", "company": "Mila Quebec AI Institute"}
    CrewaiEnterpriseContentMarketingCrew().crew().kickoff(inputs=inputs)


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {"topic": "AI for Science", "company": "Mila Quebec AI Institute"}
    try:
        CrewaiEnterpriseContentMarketingCrew().crew().train(
            n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs
        )

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")


def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        CrewaiEnterpriseContentMarketingCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")


def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {"topic": "AI Agent Framework", "company": "CrewAI"}
    try:
        CrewaiEnterpriseContentMarketingCrew().crew().test(
            n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs
        )

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")
