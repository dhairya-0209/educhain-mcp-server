"""
Standalone FastAPI server exposing your mock EduChain tools.
Works even with the very old MCP build that only supports stdio.
"""

from fastapi import FastAPI, Body
from pydantic import BaseModel
from educhain_content import make_mcqs, lesson_plan, flash_cards

app = FastAPI(title="EduChain‑MCP (mock)", version="0.1")

# ───────────── Health check ─────────────
@app.get("/health")
def health():
    return {"status": "ok"}

# ─────────── Tool: MCQ generator ────────
class MCQRequest(BaseModel):
    topic: str = "Python"
    num_questions: int = 5

@app.post("/v1/tool/generate_mcqs")
def api_generate_mcqs(req: MCQRequest):
    return make_mcqs(req.topic, req.num_questions)

# ────────── Tool: Flashcards ────────────
class CardRequest(BaseModel):
    topic: str = "Python"
    n: int = 5

@app.post("/v1/tool/flashcards")
def api_flashcards(req: CardRequest):
    return flash_cards(req.topic, req.n)

# ─────── Resource: Lesson Plan (GET) ────
@app.get("/v1/resource/lesson/{topic}")
def api_lesson(topic: str):
    return lesson_plan(topic)

# ──────────── Run with uvicorn ──────────
if __name__ == "__main__":
    import uvicorn
    print("🚀  FastAPI server running on http://localhost:8000")
    uvicorn.run("mcp_server:app", host="0.0.0.0", port=8000, reload=True)
