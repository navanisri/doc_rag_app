from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class QuestionRequest(BaseModel):
    question: str

@router.post("/")
async def answer_question(request: QuestionRequest):
    question = request.question.lower()
    if "name" in question:
        return {"answer": "This is a Document Management and Q&A API built with FastAPI."}
    elif "weather" in question:
        return {"answer": "I don't have real-time data, but you can check a weather website!"}
    else:
        return {"answer": "I'm not sure how to answer that. Try a different question."}
