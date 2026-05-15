from typing import Dict
from app.agents.evaluation_agent import generate_ai_feedback
from app.db.models.evaluation_model import Evaluation
from app.db.models.quiz_model import Quiz
from app.db.models.user_answers_model import UserAnswer


def evaluate_quiz(db, quiz_id, answers: Dict):

    attempt = Evaluation(
        quiz_id=quiz_id,
        score=0,
        percentage=0
    )

    db.add(attempt)
    db.commit()
    db.refresh(attempt)

    quiz = db.query(Quiz).filter(Quiz.id == quiz_id).first()

    if not quiz:
        return {
            "success": False,
            "error":"Invalid Quiz: Quiz not found!"
        }
    
    questions = quiz.questions
    total = len(questions)
    score = 0
    results = []

    for q in questions:

        user_answer = answers.get(str(q.id))

        is_correct = q.correct_answer.lower() == user_answer.lower()

        if is_correct:
            score += 1

        user_answer_obj = UserAnswer(
            question_id = q.id,
            selected_answer = user_answer,
            is_correct = is_correct
        )
        db.add(user_answer_obj)
        results.append({
            "question_id": q.id,
            "question": q.question,
            "your_answer": user_answer,
            "correct_answer": q.correct_answer,
            "is_correct": is_correct
        })

    percentage = (score / total) * 100

    feedback = generate_ai_feedback(
        topic=quiz.topic,
        result=results,
        percentage=percentage
    )
    
    attempt.feedback = feedback
    attempt.score = score
    attempt.percentage = (score / total) * 100

    db.commit()
    db.refresh(attempt)
    return {
        "success": True,
        "score": score,
        "total": total,
        "percentage": percentage,
        "feedback": feedback,
        "results": results
    }