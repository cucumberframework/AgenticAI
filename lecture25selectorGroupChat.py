import asyncio

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.conditions import MaxMessageTermination, TextMentionTermination
from autogen_agentchat.teams import SelectorGroupChat
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient
from dotenv import load_dotenv

load_dotenv()


async def main():
    model_client = OpenAIChatCompletionClient(model="gpt-4o")
    agent1 = AssistantAgent(name="TestPlanner", model_client=model_client,
                            system_message="You are expert in creating test cases and test plan for the given webpage you will analyze all the possible scenarios and create the test plan and test cases"
                                           "You can run through the application and analyze all the positive and negative test cases and create the test case and test plan")
    agent2 = AssistantAgent(name="Generator", model_client=model_client,
                            system_message="you are the generator agent and has capability to generate the Playwright javascript test scripts based on the test plan or test cases provided by the Test planner agent "
                                           "While creating the test scripts you should follow all standard page object model for Industry standard automation framework")
    agent3 = AssistantAgent(name="Healer", model_client=model_client,
                            system_message="You are healer agent who can fix the failed test cases after analyzing the failed test scripts you have capability to rerun the failed test scripts and fix the same "
                                           "Once you are satisfied with test script which you have created, you can terminate or when you see 'TERMINATE' message which is provided by you ")

    terminationcondition=MaxMessageTermination(max_messages=10) | TextMentionTermination("TERMINATE")
    teamchat= SelectorGroupChat([agent1,agent2,agent3],termination_condition=terminationcondition,model_client=model_client)
    await Console(teamchat.run_stream(task="Analyze the https://www.naukri.com login page and create the test plan and Generator agent should create the playwright javascript test scripts for the same"))
asyncio.run(main())
