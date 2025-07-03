# 🧠 EduChain MCP Server (Mock)

This project simulates a Claude-compatible **MCP (Multi-Channel Plugin) Server** for educational content generation — built with **FastAPI** and returning **mock data** (no OpenAI key required).

> ✅ Compatible with [Claude Desktop](https://www.anthropic.com)  
> ✅ No internet or API key required  
> ✅ Perfect for local demos, submissions, and offline use

---

## ✨ Features

 ✅ Generate **Multiple Choice Questions (MCQs)** on any topic
 
 ✅ Provide a **lesson plan** with objectives and activities
 
 ✅ Return **flashcards** for fast revision
 
 ✅ FastAPI server with clean JSON APIs
 
 ✅ Works fully offline using mocked responses

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

📁 `mcp_server.py` – FastAPI server entry point

📁 `educhain_content.py` – Generates mock MCQs, flashcards, and lesson plans

📁 `requirements.txt` – All Python dependencies

📁 `sample_sessions/commands.txt` – API requests made during testing


📁 `sample_sessions/responses.json` – Expected responses to test requests

📁 `config/claude_desktop_config.json` – Claude Desktop MCP config (HTTP URL)

📁 `README.md` – Full project documentation (this file)

--- 

## ⚙️ Setup Instructions

### 1. Clone the repository

git clone https://github.com/dhairya-0209/educhain-mcp-server.git

cd educhain-mcp-server

### 2. Create & activate virtual environment

python -m venv .venv

.venv\Scripts\activate  # For Windows

### 3. Install required packages

pip install -r requirements.txt

### 4. Run the FastAPI server

python mcp_server.py

✅ Server will start at: http://localhost:8000

---

## 🔌 Claude Desktop Integration

- Open Claude Desktop → Settings → MCP Configuration

- Upload config/claude_desktop_config.json

 {
 
  "mcp_server": {
  
    "transport": "http",
    
    "url": "http://localhost:8000"
    
  }
}

You can now ask Claude:

- “Generate 5 MCQs on Python”

- “Give me a lesson plan on OOP”

- “Create flashcards on Data Structures”

  ---


## 📡 API Reference


| 🛠 Method | 🔗 Endpoint                   | 📄 Purpose                 |
| --------- | ----------------------------- | -------------------------- |
| `GET`     | `/health`                     | Health check               |
| `POST`    | `/v1/tool/generate_mcqs`      | Generate mock MCQs         |
| `GET`     | `/v1/resource/lesson/{topic}` | Get structured lesson plan |
| `POST`    | `/v1/tool/flashcards`         | Generate flashcards        |

---

### 1️⃣ Generate MCQs

POST /v1/tool/generate_mcqs

Content-Type: application/json

{

  "topic": "Python",
  
  "num_questions": 3
  
}


### Response ▶️

[

  {
  
    "question": "What is Python?",
    
    "options": ["A concept", "A tool", "An app", "None"],
    
    "answer": "A concept"
    
  }
  
]


### 2️⃣ Lesson Plan

GET /v1/resource/lesson/Python

### Response ▶️

{

  "title": "Lesson Plan for Python",
  
  "objectives": [
  
    "Understand basics of Python",
    
    "Explore examples of Python"
    
  ],
  
  "content": "This lesson will introduce the core concepts of Python.",
  
  "activities": ["Watch video", "Solve quiz", "Group discussion"]
  
}


### 3️⃣ Flashcards

POST /v1/tool/flashcards

Content-Type: application/json

{

  "topic": "Python",
  
  "n": 3
  
}

### Response ▶️

[

  {
  
    "term": "Python Term 1",
    
    "definition": "This is the definition of Python Term 1."
    
  }
  
]

---  

## 🧪 Sample Session Files

sample_sessions/commands.txt → all test calls made

sample_sessions/responses.json → expected mock outputs

---



