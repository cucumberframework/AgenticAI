import asyncio
import os

import console
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient
from dotenv import load_dotenv
load_dotenv()

async def main1():
    print("I am inside function")

    api_model_client = OpenAIChatCompletionClient(
        model="gpt-4o")
    assistant= AssistantAgent(name="assistant",model_client=api_model_client)

    stream=assistant.run_stream(task="Capital of Nagaland")
    await Console(stream)
    await api_model_client.close()

if __name__ == "__main__":
    asyncio.run(main1())