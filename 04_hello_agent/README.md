# Gemini Chatbot

A simple chatbot using the Gemini API integrated with Python’s `openai` library. This project uses the `AsyncOpenAI` client to communicate with Gemini models and handle chat interactions asynchronously.

---

## ✨ Features

- **Asynchronous interaction**: Uses `asyncio` for smooth, non-blocking execution.
- **Environment-based configuration**: API keys and URLs loaded from `.env`.
- **Simple agent with instructions**: The chatbot is configured to avoid special formatting characters in responses.
- **Customizable agent**: Uses Gemini’s `openai_client` with model `"gemini-2.0-flash"`.

---

## 🛠️ Prerequisites

- Python 3.8+
- Gemini API key (obtainable from your Gemini account)
- Base URL for Gemini API

---

## 📦 Installation

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd <your-project-directory>
````

2. **Create a virtual environment:**

   ```bash
   uv venv
   ```

3. **Activate the environment:**

   * On Windows:

     ```bash
     .venv\Scripts\activate
     ```
   * On Mac/Linux:

     ```bash
     source .venv/bin/activate
     ```

4. **Install dependencies:**

   ```bash
   uv add python-dotenv openai
   ```

---

## ⚙️ Configuration

Create a `.env` file in the root directory and add your Gemini API key and Base URL:

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
GEMINI_BASE_URL=YOUR_GEMINI_BASE_URL
```

Replace `YOUR_GEMINI_API_KEY` with your actual API key.

---

## 🚀 Running the Chatbot

Run the chatbot using:

```bash
uv run python chatbot.py
```

You can also run directly with:

```bash
python chatbot.py
```

---

## 👩‍💻 Author

**Shumaila Waheed**

---

## 📑 License

This project is licensed under the MIT License.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to open a pull request.

---

## 📝 Notes

* Make sure your Gemini API key is correct and has access to the specified model.
* Double-check that the `base_url` matches your Gemini environment.

```

