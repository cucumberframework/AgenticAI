import asyncio

from autogen_agentchat.agents import AssistantAgent, UserProxyAgent
from autogen_agentchat.conditions import TextMentionTermination
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient
from dotenv import load_dotenv

load_dotenv()


async def main():
    model_client = OpenAIChatCompletionClient(model="gpt-4o")
    agent1 = AssistantAgent(name="Teacher", model_client=model_client,
                            system_message="You are expert of world geopolitics and should help me to understand who is correct in Iran USA war "
                            "When you see 'THANK YOU' or any similar word of Appreciate terminate the chat after thanking him back")

    user=UserProxyAgent(name="Student")

    round=RoundRobinGroupChat([user,agent1],termination_condition=TextMentionTermination("Done"))

    await Console(round.run_stream(task="Why is war going on in gulf region "))


asyncio.run(main())
