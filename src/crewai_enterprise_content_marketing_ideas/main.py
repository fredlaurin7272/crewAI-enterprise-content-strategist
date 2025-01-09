#!/usr/bin/env python

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

