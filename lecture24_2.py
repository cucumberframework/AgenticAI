import asyncio
import json

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient
from dotenv import load_dotenv
load_dotenv()

async def main():
    model_client=OpenAIChatCompletionClient(model="gpt-4o")
    agent1=AssistantAgent(name="agentOne",model_client=model_client)
    agent2=AssistantAgent(name="AgentTwo",model_client=model_client)
    await Console(agent1.run_stream(task="My favorite colour is red"))
    state=await agent1.save_state()
    with open("memory.json","w") as f:
        json.dump(state,f,default=str)

    with open("memory.json","r") as f:
        memory=json.load(f)
        await agent2.load_state(memory)

    await Console(agent2.run_stream(task="What is my favorite colour?"))


asyncio.run(main())