# 🧠 EduChain MCP Server (Mock)

This project simulates a Claude-compatible **MCP (Multi-Channel Plugin) Server** for educational content generation — built with **FastAPI** and returning **mock data** (no OpenAI key required).

> ✅ Compatible with [Claude Desktop](https://www.anthropic.com)  
> ✅ No internet or API key required  
> ✅ Perfect for local demos, submissions, and offline use

---

## ✨ Features

- ✅ Generate **Multiple Choice Questions (MCQs)** on any topic
- ✅ Provide a **lesson plan** with objectives and activities
- ✅ Return **flashcards** for fast revision
- ✅ FastAPI server with clean JSON APIs
- ✅ Works fully offline using mocked responses

---

## 🏗️ Technologies Used

| Tech         | Description                         |
|--------------|-------------------------------------|
| Python       | Core programming language           |
| FastAPI      | API framework for serving endpoints |
| Uvicorn      | ASGI server                         |
| Pydantic     | Request validation                  |
| curl/Postman | API testing                         |
| Claude MCP   | Final target integration            |

---

## 🗂️ Folder Structure

educhain-mcp-server/
├── mcp_server.py # FastAPI server
├── educhain_content.py # Mock logic for MCQ, lesson, flashcards
├── requirements.txt # Python dependencies
├── sample_sessions/
│ ├── commands.txt # API calls made
│ └── responses.json # Their responses
├── config/
│ └── claude_desktop_config.json # Claude MCP config (local server URL)
└── README.md



---

## ⚙️ Setup Instructions

1. **Clone the repo**
   
   - git clone https://github.com/dhairya-0209/educhain-mcp-server.git
   
   - cd educhain-mcp-server
   
   - Create and activate virtual environment

    - python -m venv .venv

    .venv\Scripts\activate   # for Windows
   
    Install required packages

    pip install -r requirements.txt
   
    Run the FastAPI server


python mcp_server.py

✅ Server will start at: http://localhost:8000

🔌 Claude Desktop Integration

In Claude Desktop, open Settings → MCP Configuration

Upload this config:

{
  "mcp_server": {
    "transport": "http",
    "url": "http://localhost:8000"
  }
}

Now Claude can call:

generate_mcqs

lesson_plan

flashcards

🔍 API Reference

🧠 1. Generate MCQs
POST /v1/tool/generate_mcqs

Request body:

{
  "topic": "Python",
  "num_questions": 3
}

Sample response:

[
  {
    "question": "What is Python?",
    "options": ["A concept", "A tool", "An app", "None"],
    "answer": "A concept"
  },
  ...
]

📚 2. Lesson Plan

GET /v1/resource/lesson/Python

Response:

{
  "title": "Lesson Plan for Python",
  "objectives": ["Understand basics of Python", "Explore examples of Python"],
  "content": "This lesson will introduce the core concepts of Python.",
  "activities": ["Watch video", "Solve quiz", "Group discussion"]
}

🔁 3. Flashcards

POST /v1/tool/flashcards

Request:

{
  "topic": "Python",
  
  "n": 3
}
Sample response:

[
  {
    "term": "Python Term 1",
    
    "definition": "This is the definition of Python Term 1."
    
  },
  
  ...
]

🧪 Sample Session Files

sample_sessions/commands.txt → all 3 tested calls

sample_sessions/responses.json → their exact mock responses

