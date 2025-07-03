# educhain_content.py
"""
Mocked EduChain functions – no OpenAI key needed
"""

def make_mcqs(topic: str, n: int = 5):
    return [
        {
            "question": f"What is {topic}?",
            "options": ["A concept", "A tool", "An app", "None"],
            "answer": "A concept"
        }
        for _ in range(n)
    ]

def lesson_plan(topic: str):
    return {
        "title": f"Lesson Plan for {topic}",
        "objectives": [f"Understand basics of {topic}", f"Explore examples of {topic}"],
        "content": f"This lesson will introduce the core concepts of {topic}.",
        "activities": ["Watch video", "Solve quiz", "Group discussion"]
    }

def flash_cards(topic: str, n: int = 5):
    return [
        {
            "term": f"{topic} Term {_+1}",
            "definition": f"This is the definition of {topic} Term {_+1}."
        }
        for _ in range(n)
    ]


# Quick test
if __name__ == "__main__":
    import json
    print(json.dumps(make_mcqs("Python Loops", 3), indent=2))
