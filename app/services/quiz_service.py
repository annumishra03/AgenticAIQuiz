import json

from requests import Session
from app.agents.quiz_agent import generate_quiz
from app.db.models.questions_model import Question
from app.db.models.quiz_model import Quiz
from app.schemas.quiz_schema import QuizQuestion
from app.utills.json_parser import parse_json_response

def generate_quiz_flow(db, topic, num_questions):

    try:
        quiz_text = generate_quiz(topic, num_questions)
        quiz = parse_json_response(quiz_text)

        if quiz is None:
            return {
                "success": False,
                "error": "AI returned Invalid data"
            }
        
        valid_quiz = validate_quiz(quiz)

        if len(valid_quiz) > 0:
            quiz = save_quiz(db, topic, valid_quiz)
            return {
                "success": True,
                "quiz_id": quiz.id,
                "quiz": [
                    {
                        "id": q.id,
                        "question": q.question,
                        "options": q.options
                    }
                    for q in quiz.questions
                ]
            }
        else:
            return {
                "success": False,
                "error": "AI returned invalid questions"
            }
    except json.JSONDecodeError:
        return {
            "success": False,
            "error": "AI returned invalid JSON"
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }
    
def validate_quiz(quiz_data: dict):
    validated_quiz = []
        
    questions_list = quiz_data.get("questions", [])
    for question in questions_list:
        try:
            if isinstance(question, dict):
                validated_quiz.append(QuizQuestion(**question))
            else:
                print("Skipping invalid item:", question)
        except Exception as e:
            print("Skipping invalid question:", e)

    
    return validated_quiz

def save_quiz(db: Session, topic: str, quiz_data: list):

    quiz = Quiz(topic=topic)
    # print(quiz_data)
    for q in quiz_data:
        question = Question(
            question=q.question,
            options=q.options,
            correct_answer=q.answer
        )
        quiz.questions.append(question)

    db.add(quiz)
    db.commit()
    db.refresh(quiz)
    print(quiz)
    return quiz