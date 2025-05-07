#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from cleeroute.crew import Cleeroute

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
    Run the crew.
    """
    topic = "digital marketing"
    objective = """
        - Understand the fundamentals of digital marketing,
        - Master key tools,
        - Know how to create a digital strategy,
        - Create and manage campaigns,
        - Analyze and interpret results,
        - Develop an online presence.
        """

    prerequisites = """ 
        - Basic computer skills,
        - General digital literacy,
        - Analytical mindset.
    """

    inputs = {
        "topic": topic,
        "objective": objective,
        "prerequisites":prerequisites
    }
    
    try:
        Cleeroute().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        Cleeroute().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        Cleeroute().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs",
        "current_year": str(datetime.now().year)
    }
    try:
        Cleeroute().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
