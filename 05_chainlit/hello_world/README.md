# Chainlit Gemini Chatbot

A simple chatbot built with Chainlit that uses Google’s Gemini API for responses.

---

## 📋 Prerequisites

1. **Python 3.8+** installed  
2. **Chainlit** package  
3. **httpx** package  
4. **python-dotenv** package  

---

## ⚙️ Installation

1. Clone this repository or copy the project files into a new folder.  
2. Open a terminal/command prompt and navigate to the project folder.

3. (Recommended) Create a virtual environment and activate it:
   ```bash
   python -m venv .venv
   .\.venv\Scripts\activate    # Windows
   source .venv/bin/activate   # macOS/Linux
````

4. Install dependencies:

   ```bash
   pip install chainlit httpx python-dotenv
   ```

---

## 🔑 Environment Variables

1. Obtain your **GEMINI\_API\_KEY** and **GEMINI\_API\_URL** from Google Cloud.
2. In the project folder, create a file named `.env`.
3. Add the following lines to `.env`:

   ```
   GEMINI_API_KEY=YOUR_API_KEY_HERE
   GEMINI_API_URL=YOUR_API_URL_HERE
   ```

   Replace `YOUR_API_KEY_HERE` and `YOUR_API_URL_HERE` with your actual values.

---

## 📂 File Structure

```
.
├── .env                 # Contains GEMINI_API_KEY and GEMINI_API_URL
├── chatbot.py           # Main Chainlit chatbot script
└── README.md            # This file
```

---

## 🚀 Usage

1. Ensure your virtual environment is activated (if used).
2. Run the Chainlit app:

   ```bash
   chainlit run chatbot.py
   ```
3. Chainlit will start a local server (default at `http://localhost:8000`).
4. Open your browser and navigate to the provided URL to interact with the chatbot.
5. Type a message in the chat interface. The bot will send your input to Gemini and display the response.

---

## 🤖 How It Works

* **dotenv** loads `GEMINI_API_KEY` and `GEMINI_API_URL` from `.env`.

* On each incoming message, the `@cl.on_message` handler:

  1. Reads the user’s input (`message.content`).
  2. Sends an HTTP POST request to the Gemini API endpoint (`GEMINI_API_URL`) with the user’s text.
  3. Parses the JSON response to extract the generated reply.
  4. Sends the reply back to the chat interface.

* If the API URL is missing, the bot returns an error message in chat.

---

## ⚠️ Error Handling

* If there is an issue contacting Gemini (network error, invalid key, etc.), the bot will catch the exception and display:

  ```
  Error contacting Gemini API: <error details>
  ```

---

## 📈 Customization

* **GEMINI\_API\_URL**: Change this to the correct REST endpoint for your Gemini deployment if needed.
* **Request Payload**: Modify `payload` if the API schema changes or additional parameters are required.
* **Headers**: Adjust headers for authentication or content type if necessary.

---

## 📚 References

* [Chainlit Documentation](https://chainlit.dev)
* [httpx Documentation](https://www.python-httpx.org)
* [python-dotenv Documentation](https://github.com/theskumar/python-dotenv)
* [Google Vertex AI Gemini Docs](https://cloud.google.com/vertex-ai)

---

**Enjoy chatting with Gemini via Chainlit!**

```
```
