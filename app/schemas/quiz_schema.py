from typing import Dict, List, Optional
from pydantic import BaseModel, Field
from app.config import NO_OF_QUESTION,QUESTION_LIMIT

class QuizRequest(BaseModel):
    module: str = Field(..., min_length=2),
    no_of_questions: int = Field(default=NO_OF_QUESTION,ge=1,le=QUESTION_LIMIT)

class QuizQuestion(BaseModel):
    question: str
    options: List[str]
    answer: str


class QuizQuestionResponse(BaseModel):
    id: int
    question: str
    options: list[str]

class QuizResponse(BaseModel):
    success: bool
    quiz_id: Optional[int] = None
    quiz: Optional[List[QuizQuestionResponse]] = None
    error: Optional[str] = None


class QuizAnswerRequest(BaseModel):
    quiz_id: int
    answers: Dict[str,str]

class QuizAnswerResponse(BaseModel):
    success: bool
    error: Optional[str] = None
    score: int
    total: int
    percentage: float
    feedback: str


