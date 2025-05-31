import os
from dotenv import load_dotenv
from agents import Agent, AsyncOpenAI, OpenAIChatCompletionsModel,RunConfig,Runner
from pydantic import config



# Load .env file
load_dotenv()

# Get API key from environment
gemini_api_key = os.getenv("gemini_API_KEY")


if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")

#Reference: https://ai.google.dev/gemini-api/docs/openai
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

agent = Agent(
    name="Translation Agent",
    instructions="You are a helpful assistant that translates text from Urdu to English.",

)

response = Runner.run_sync(
    agent,
    input="میں فل اسٹیک ڈویلپر بننے کے لیے پائتھون پروگرامنگ سیکھ رہا ہوں۔",
    run_config=config
)


print(response)








