# Simple Agent Chat Simulation

This project demonstrates a basic simulation where two agents communicate with each other by sending and receiving messages.

## 🚀 Features

- Two agents: `Agent_Alpha` and `Agent_Beta`.
- Each agent sends a random message and mood to the other agent.
- Simulates typing animation before sending a message.

## 🛠️ Requirements

- Python 3.8 or higher.

## 📝 How to Run

1. **Clone the repository** or download the project folder.

2. **Navigate to the project directory**:
   ```bash
   cd chatbot
````

3. **(Optional) Create a virtual environment using `uv`**:

   ```bash
   uv venv
   ```

4. **Activate the virtual environment**:

   * On macOS/Linux:

     ```bash
     source .venv/bin/activate
     ```
   * On Windows:

     ```bash
     .venv\Scripts\activate
     ```

5. **Install dependencies**:

   ```bash
   uv pip install -r requirements.txt
   ```

6. **Run the project**:

   ```bash
   uv run python main.py
   ```

## 📦 File Structure

```
chatbot/
│
├── main.py              # Main Python script
├── requirements.txt     # Dependencies
└── README.md            # Project documentation
```

## 📝 Notes

* No API keys or environment variables are required for this project.
* This is a beginner-friendly example to understand how agents can communicate with each other in Python.
