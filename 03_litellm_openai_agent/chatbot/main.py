from litellm import completion, exceptions
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("VERTEXAI_API_KEY")

def get_user_input():
    return input("You: ")

def get_gemini_response(user_message):
    try:
        response = completion(
            model="gemini/gemini-1.5-flash",
            messages=[{"role": "user", "content": user_message}],
            api_key=API_KEY
        )
        return response['choices'][0]['message']['content']
    except exceptions.OpenAIError as e:
        return f"⚠️ LiteLLM Error: {e}"

def main():
    print("💬 Gemini Chatbot started. Type 'exit' to quit.\n")
    while True:
        user_message = get_user_input()
        if user_message.lower() in ["exit", "quit"]:
            print("👋 Exiting chat. Goodbye!")
            break
        gemini_response = get_gemini_response(user_message)
        print(f"Gemini: {gemini_response}")
        print("-" * 50)

if __name__ == "__main__":
    main()
