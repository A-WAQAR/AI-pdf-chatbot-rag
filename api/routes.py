from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from utils.rag_pipeline import run_rag

router = APIRouter()
class QuestionRequest(BaseModel):
    question: str

@router.get("/")
def home():
    return {
        "message": "PDF RAG API is running"
    }

@router.post("/ask")
def ask_question(request: QuestionRequest):

    question = request.question.strip()

    if not question:
        raise HTTPException(status_code=400, detail="question cannot be empty")
    from main import vectorstore_obj
    answer = run_rag(vectorstore_obj, question)

    return {
        "question": question,
        "answer": answer
    }

