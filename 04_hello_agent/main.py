import os
import asyncio
from dotenv import load_dotenv
from openai import AsyncOpenAI
from agents import Agent, OpenAIChatCompletionsModel, Runner, set_tracing_disabled

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")
gemini_base_url = os.getenv("GEMINI_BASE_URL")

if not gemini_api_key or not gemini_base_url:
    raise ValueError("API key or Base URL not found in environment variables.")

client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url=gemini_base_url
)

set_tracing_disabled(True)

async def main():
    agent = Agent(
        name="Assistant",
        instructions=(
            "You are a helpful assistant. "
            "Do not use asterisks ** or any special formatting characters in your response."
        ),
        model=OpenAIChatCompletionsModel(
            model="gemini-2.0-flash",
            openai_client=client
        )
    )

    result = await Runner.run(
        agent,
        "What is programming?"
    )

    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())
