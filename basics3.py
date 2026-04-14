import asyncio
import os

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.conditions import MaxMessageTermination
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient
from dotenv import load_dotenv
load_dotenv()

async def main():
    print("I am inside main")
    model_client = OpenAIChatCompletionClient(model="gpt-4.1")
    agent1 = AssistantAgent(name="MathTeacher", model_client=model_client,
                            system_message="You are expert of Playwright Automation with Javascript with CI CD pipeline and all related Automation testing technology,act as expert teacher and answer all the queries which are asked by your teacher and start the discussion with student ")

    agent2 = AssistantAgent(name="StudentOfAutomationTesting", model_client=model_client,
                            system_message="You are student of Automation testing who is learning Automation and you have some queries which you need to resolve")

    team=RoundRobinGroupChat([agent1,agent2],termination_condition=MaxMessageTermination(max_messages=6))
    await Console(team.run_stream(task="lets Discuss your queries on Automation testing with Playwright javascript"))

asyncio.run(main())
