import asyncio
import os
from autogen_core import Image
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.messages import MultiModalMessage
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient
from openai import images
from dotenv import load_dotenv
load_dotenv()


async def multimediaMessageVerification():
    print("I am inside function")

    api_model_client = OpenAIChatCompletionClient(model="gpt-4.1")
    assistant = AssistantAgent(name="multimodalAssistant", model_client=api_model_client)
    image = Image.from_file("C:/Users/Meetanshi/Desktop/MultiImage.jpeg")
    multimodalMessage = MultiModalMessage(content=["Find matching images ?", image], source="user")
    await Console(assistant.run_stream(task=multimodalMessage))
    await api_model_client.close()


if __name__ == "__main__":
    asyncio.run(multimediaMessageVerification())
