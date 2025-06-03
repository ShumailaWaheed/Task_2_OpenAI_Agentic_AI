# 🤖 Gemini Chatbot with Rate Limiting and Error Handling

This project implements a chatbot using Google's Gemini AI models with Chainlit, featuring rate limiting, dynamic model switching, and error handling. It ensures responsible API usage and a smooth user experience even during API rate limit or quota errors.

---

## Features 🚀

✅ **Chainlit Integration**: Seamless integration with Chainlit for interactive chat.  
✅ **Google Gemini AI**: Leverages powerful Gemini models for natural language understanding and response generation.  
✅ **Rate Limiting**: Implements per-minute and daily rate limits with exponential backoff to prevent hitting API quotas.  
✅ **Model Switching**: Automatically switches to alternative Gemini models if the preferred model is unavailable.  
✅ **Error Handling**: Detects and manages errors like rate limit exceedance and model unavailability with informative user feedback.  
✅ **Environment Variable Support**: Loads the Gemini API key from a `.env` file for secure key management.

---

## Prerequisites 🛠️

- Python 3.8+
- A Google Gemini API Key
- Node.js & npm (optional, if using Chainlit frontend)

---

## Setup ⚙️

1️⃣ **Clone the repository:**
```bash
git clone https://github.com/yourusername/gemini-chatbot.git
cd gemini-chatbot
````

2️⃣ **Create a `.env` file:**

```env
GEMINI_API_KEY=your_google_gemini_api_key_here
```

3️⃣ **Install dependencies:**

```bash
pip install -r requirements.txt
```

4️⃣ **Run the Chainlit app:**

```bash
chainlit run main.py
```

---

## Usage 📝

* When the chatbot starts, it checks available Gemini models.
* Automatically chooses the best available Gemini model.
* Handles per-minute and daily rate limits with smart retries.
* Provides user-friendly error messages when rate limits are hit or models are unavailable.
* Offers fallback model switching if the preferred model is not found.

---

## Project Structure 📁

```
gemini-chatbot/
├── main.py           # Main Python script with Chainlit and Gemini integration
├── .env              # Environment variable file for your API key
├── requirements.txt  # Python dependencies
└── README.md         # Project documentation
```

---

## Customization ✨

* **Rate Limiting**: Adjust `max_requests_per_minute` and `max_requests_per_day` in the `RateLimiter` class to suit your usage patterns.
* **Model Preferences**: Change the preferred model names in the script as needed.
* **Error Messages**: Customize error handling messages in the `main.py` script.

---

## Contributing 🤝

Contributions are welcome! Please fork the repository and submit a pull request with your improvements.

---

## License 📄

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Author ✍️

**Shumaila Waheed**

---

## Contact 📬

For questions or support, please reach out via GitHub Issues.

---

Happy Coding! 🎉

```
