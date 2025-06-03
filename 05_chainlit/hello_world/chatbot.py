import os
import time
import random
import asyncio
from dotenv import load_dotenv
import chainlit as cl
import google.generativeai as genai
from google.api_core.exceptions import ResourceExhausted

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise EnvironmentError("GEMINI_API_KEY is not set in .env file.")

# Configure API
genai.configure(api_key=api_key)

# --- Rate Limiter Class ---
class RequestLimiter:
    def __init__(self, per_minute=10, per_day=800):
        self.per_minute = per_minute
        self.per_day = per_day
        self.minute_count = 0
        self.daily_count = 0
        self.last_minute_check = time.time()
        self.last_day_check = time.time()

    def reset_counters(self):
        current = time.time()
        if current - self.last_minute_check >= 60:
            self.minute_count = 0
            self.last_minute_check = current
        if current - self.last_day_check >= 86400:
            self.daily_count = 0
            self.last_day_check = current

    async def wait_if_needed(self):
        self.reset_counters()
        if self.minute_count >= self.per_minute:
            wait = 60 - (time.time() - self.last_minute_check)
            print(f"[RateLimiter] Per-minute limit reached. Waiting {wait:.1f} seconds...")
            await asyncio.sleep(wait)
            self.reset_counters()
        if self.daily_count >= self.per_day:
            wait = 86400 - (time.time() - self.last_day_check)
            print(f"[RateLimiter] Daily limit reached. Waiting {wait:.1f} seconds...")
            await asyncio.sleep(wait)
            self.reset_counters()

    def increment(self):
        self.minute_count += 1
        self.daily_count += 1

# Instantiate RateLimiter
rate_limiter = RequestLimiter()

# --- Model Selection ---
def select_model(available):
    preferred = [
        "models/gemini-2.0-flash",
        "models/gemini-1.5-flash",
        "models/gemini-1.5-flash-latest"
    ]
    for name in preferred:
        if name in available:
            return name
    for name in available:
        if "gemini" in name.lower():
            return name
    raise ValueError("No suitable Gemini model found.")

# Fetch available models
try:
    models = genai.list_models()
    model_names = [m.name for m in models]
    selected_model = select_model(model_names)
    print(f"[Model] Selected: {selected_model}")
except Exception as e:
    print(f"[Model] Error fetching models: {e}")
    selected_model = "models/gemini-2.0-flash"  

# --- Model Configuration ---
generation_config = {
    "temperature": 0.7,
    "top_p": 0.9,
    "max_output_tokens": 1500
}

safety = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"}
]

model = genai.GenerativeModel(
    model_name=selected_model,
    generation_config=generation_config,
    safety_settings=safety
)

chat_session = None

# --- Chainlit Handlers ---
@cl.on_chat_start
async def handle_chat_start():
    global chat_session
    chat_session = model.start_chat(history=[])
    await cl.Message("Hello! How can I help you today?").send()

@cl.on_message
async def handle_message(message: cl.Message):
    global chat_session
    try:
        if chat_session is None:
            chat_session = model.start_chat(history=[])

        await rate_limiter.wait_if_needed()

        thinking = await cl.Message("Let me think...").send()

        max_retries = 4
        attempt = 0
        backoff = 2

        while attempt < max_retries:
            try:
                reply = chat_session.send_message(message.content)
                rate_limiter.increment()
                await thinking.remove()
                await cl.Message(reply.text).send()
                break
            except ResourceExhausted:
                attempt += 1
                wait_time = backoff + random.uniform(0, 1)
                await thinking.remove()
                thinking = await cl.Message(f"Rate limit hit. Retrying in {wait_time:.1f} seconds...").send()
                await asyncio.sleep(wait_time)
                backoff *= 2
        else:
            await thinking.remove()
            await cl.Message("Sorry, I couldn't process your request after multiple attempts. Please try again later.").send()

    except Exception as e:
        await cl.Message(f"An error occurred: {str(e)}").send()
