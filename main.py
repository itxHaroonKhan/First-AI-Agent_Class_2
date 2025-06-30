
import os
from dotenv import load_dotenv
from agents import Agent, AsyncOpenAI, RunConfig, Runner, OpenAIChatCompletionsModel


load_dotenv()

API = os.getenv("API_KEY")


client = AsyncOpenAI(api_key=API,base_url="https://generativelanguage.googleapis.com/v1beta/openai/")


model = OpenAIChatCompletionsModel(
    model = "gemini-2.0-flash",
     openai_client=client
)

config = RunConfig(model=model, model_provider=client, tracing_disabled=True)

agent = Agent(
    name = "Gemini Agent",
    instructions = "Your Name is Haroon and you are a helpful assistant."
)


say = input("How can I help you? ")

response = Runner.run_sync(
    agent,
    input= say,
    run_config=config
)


print(response.final_output)
