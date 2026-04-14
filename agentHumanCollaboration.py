import asyncio


from autogen_agentchat.agents import AssistantAgent, UserProxyAgent
from autogen_agentchat.conditions import TextMentionTermination
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient

from dotenv import load_dotenv
load_dotenv()

async def main():
    model_client = OpenAIChatCompletionClient(model="gpt-4.1")
    agent = AssistantAgent(name="PlaywrightExpertWithJs", model_client=model_client,
                           system_message="You are Expert in Playwright Javascript and all related technology of automation "
                                          "You can close the chat when you see input message as 'Done' or similar to it if you feel that your answer has satisfied the user with your answer, but you need to make sure that user has entered the satisfactory input of termination")
    userchat=UserProxyAgent(name="Student")
    roundchat=RoundRobinGroupChat([userchat,agent],termination_condition=TextMentionTermination("Done::Thanks for the contacting us. Closing this session"))
    await Console(roundchat.run_stream(task="Welcome to expert chat of playwright, How can i solve your playwright Queries? "))

asyncio.run(main())
