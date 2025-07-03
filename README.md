# 🧠 EduChain MCP Server (Mock)

This project simulates a Claude-compatible **MCP server** for educational content generation — built with **FastAPI** and returns **mock data** (no API key required).

> ✅ Works with Claude Desktop MCP  
> ✅ No OpenAI or internet needed  
> ✅ Perfect for demos, testing, assignments

---

## ✨ Features

- ✅ Generate Multiple Choice Questions (MCQs)
- ✅ Create Lesson Plans
- ✅ Produce Flashcards for quick revision
- ✅ Works offline with FastAPI + Mock logic
- ✅ Claude MCP integration ready

---

## 🗂️ Folder Structure

- 📁 `mcp_server.py` – FastAPI server entry point
- 📁 `educhain_content.py` – Generates mock MCQs, flashcards, and lesson plans
- 📁 `requirements.txt` – All Python dependencies
- 📁 `sample_sessions/commands.txt` – API requests made during testing
- 📁 `sample_sessions/responses.json` – Expected responses to test requests
- 📁 `config/claude_desktop_config.json` – Claude Desktop MCP config (HTTP URL)
- 📁 `README.md` – Full project documentation (this file)

--- 

## ⚙️ Setup Instructions


 1. Clone the repository
git clone https://github.com/dhairya-0209/educhain-mcp-server.git
cd educhain-mcp-server

2. Create & activate virtual environment
python -m venv .venv
.venv\Scripts\activate  # For Windows

3. Install required packages
pip install -r requirements.txt

 4. Run the FastAPI server
python mcp_server.py

✅ Server will start at: http://localhost:8000

---

## 🔌 Claude Desktop Integration

In Claude Desktop, open Settings → MCP Configuration

Upload this config:

json
Copy
Edit

{
  "mcp_server": {
    "transport": "http",
    "url": "http://localhost:8000"
  }
}

 - Now Claude can call:

  1.generate_mcqs

  2.lesson_plan

  3.flashcards

   ---

## 📡 API Reference

🧠 1. Generate MCQs

http
Copy
Edit

POST /v1/tool/generate_mcqs
Content-Type: application/json

Request Body


Copy
Edit

{
  "topic": "Python",
  "num_questions": 3
}

📚 2. Lesson Plan

http
Copy
Edit

GET /v1/resource/lesson/Python

🔁 3. Flashcards

http
Copy
Edit

POST /v1/tool/flashcards
Content-Type: application/json

Request Body

json
Copy
Edit

{
  "topic": "Python",
  "n": 3
}

---  

## 🧪 Sample Session Files

sample_sessions/commands.txt → all test calls made

sample_sessions/responses.json → expected mock outputs

---

## 🛠️ Tech Stack

- Python 3.9+

- FastAPI

- Uvicorn

- Pydantic

- Claude Desktop (for testing MCP)

 ---

