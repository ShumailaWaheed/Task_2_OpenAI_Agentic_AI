import chainlit as cl
import httpx
import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_API_URL = os.getenv("GEMINI_API_URL")  

print("GEMINI_API_URL:", GEMINI_API_URL)

@cl.on_message
async def main(message: cl.Message):
    user_input = message.content

    headers = {
        "Authorization": f"Bearer {GEMINI_API_KEY}",
        "Content-Type": "application/json",
    }
    payload = {
        "contents": [
            {
                "parts": [{"text": user_input}]
            }
        ]
    }

    if not GEMINI_API_URL:
        await cl.Message(content="❌ Gemini API URL not configured.").send()
        return

    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(GEMINI_API_URL, json=payload, headers=headers)
            response.raise_for_status()
            data = response.json()
            gemini_reply = data.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "No reply from Gemini API.")

        except Exception as e:
            gemini_reply = f"Error contacting Gemini API: {e}"

    await cl.Message(content=gemini_reply).send()
