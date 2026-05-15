from fastapi import APIRouter, Depends, HTTPException
from requests import Session
from app.db.models.quiz_model import Quiz
from app.db.session import get_db
from app.rag.qa_chain import rag_answer
from app.schemas.quiz_schema import QuizAnswerRequest, QuizAnswerResponse, QuizResponse, QuizRequest
from app.services.quiz_service import generate_quiz_flow
from app.services.evaluation_service import evaluate_quiz
from app.config import NO_OF_QUESTION

router = APIRouter()

@router.post("/quiz", response_model=QuizResponse)
def create_quiz(payload:QuizRequest, db: Session = Depends(get_db)):
    try:

        result = generate_quiz_flow(db, payload.module, payload.no_of_questions)
        
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    

@router.get("/quiz/{quiz_id}")
def get_quiz(quiz_id: int, db: Session = Depends(get_db)):

    quiz = db.query(Quiz).filter(Quiz.id == quiz_id).first()

    return {
        "topic": quiz.topic,
        "questions": [
            {
                "id": q.id,
                "question": q.question,
                "options": q.options
            }
            for q in quiz.questions
        ]
    }

@router.post("/quiz/submit", response_model=QuizAnswerResponse)
def submit_quiz(payload: QuizAnswerRequest, db: Session = Depends(get_db)):

    result = evaluate_quiz(
        db,
        payload.quiz_id,
        payload.answers
    )

    return result

# ------------------------
# 2. Rag Answers
# ------------------------
@router.post("/rag/ask")
def ask_rag(payload: dict):

    question = payload["question"]

    answer = rag_answer(question)

    return {
        "question": question,
        "answer": answer
    }
