# Gemini Chatbot using LiteLLM

This project demonstrates a simple command-line chatbot powered by Google’s Gemini model via LiteLLM.

---

## 📋 Prerequisites

1. **Python 3.8+** installed  
2. **Litellm** package  
3. **python-dotenv** package  

---

## ⚙️ Installation

1. Clone this repository or copy the `chatbot.py` file into a new folder.
2. Open a terminal/command prompt and navigate to that folder.

3. (Optional but recommended) Create a virtual environment:
   ```bash
   python -m venv .venv
   .\.venv\Scripts\activate    # Windows
   source .venv/bin/activate   # macOS/Linux
````

4. Install dependencies:

   ```bash
   pip install litellm python-dotenv
   ```

---

## 🔑 API Key Setup

1. Obtain your **VERTEXAI\_API\_KEY** from Google Cloud (required for Gemini).
2. In the project folder, create a file named `.env` (same directory as `chatbot.py`).
3. Inside `.env`, add:

   ```
   VERTEXAI_API_KEY=YOUR_API_KEY_HERE
   ```

   Replace `YOUR_API_KEY_HERE` with your actual key.

---

## 📂 File Structure

```
.
├── .env                 # Contains VERTEXAI_API_KEY
├── chatbot.py           # Main Gemini chatbot script
└── README.md
```

---

## 🚀 Usage

1. Make sure your virtual environment is activated (if used).
2. Run the chatbot script:

   ```bash
   python chatbot.py
   ```
3. You should see:

   ```
   💬 Gemini Chatbot started. Type 'exit' to quit.
   ```
4. Type any message after the `You:` prompt. The bot will respond with Gemini’s answer.
5. To quit, type `exit` or `quit`.

---

## 🤖 How It Works

* **dotenv** loads the `VERTEXAI_API_KEY` from `.env`.
* `get_user_input()` reads user messages from the command line.
* `get_gemini_response()` calls `litellm.completion()` with:

  * `model="gemini/gemini-1.5-flash"`
  * `messages=[{"role": "user", "content": user_message}]`
  * `api_key=API_KEY`
* The bot prints Gemini’s response or an error if LiteLLM fails.

---

## ⚠️ Error Handling

If the API call fails, the script catches `litellm.exceptions.OpenAIError` and prints:

```
⚠️ LiteLLM Error: <error details>
```

---

## 📈 Customization

* **Model:** Change `model="gemini/gemini-1.5-flash"` to any supported Gemini variant.
* **Message Format:** Modify the `messages` list to include system or assistant roles if needed.
* **Environment Variables:** You can add more keys (for example, different endpoints) to the `.env` file and load them using `os.getenv()`.

---

## 📚 References

* [LiteLLM Documentation](https://github.com/litellm/litellm)
* [python-dotenv Documentation](https://github.com/theskumar/python-dotenv)
* [Google Vertex AI Docs](https://cloud.google.com/vertex-ai)

---

**Enjoy chatting with Gemini!**
