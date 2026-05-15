from fastapi import FastAPI
from app.api.routes import router
from app.db.database import Base,engine
from app.db.models.quiz_model import Quiz
from app.db.models.questions_model import Question

instance = FastAPI(title="MentorAI",version="1.0.0")
Base.metadata.create_all(bind=engine)
instance.include_router(router)

# # Import quiz generation agent
# import json
# from app.agents.quiz_agent import generate_quiz

# # Import evaluation agent
# from app.agents.evaluation_agent import evaluate_answers

# # Import progress tracking system
# from app.services.progress import save_progress

# from app.config import NO_OF_QUESTION, ANSWER_OPTIONS

# # Example module content
# # Normally this comes from completed learning module
# module = """
# Python supports variables, loops, functions, and lists.
# """


# # -----------------------------
# # STEP 1: Generate Quiz
# # -----------------------------

# print("\nGenerating Quiz...\n")

# # Call Quiz Agent
# quiz_text = generate_quiz(module)
# questions = json.loads(quiz_text)
# # Display generated quiz

# print(questions)

# # -----------------------------------
# # STEP 2: Ask User For Answers
# # -----------------------------------

# # Empty list to store answers
# answers = []
# for i, q in enumerate(questions, 1):
#     print(f"Q{i}: {q['question']}\n")  # show question only
#     for opt in q["options"]:
#         print("-", opt)
#     ans = input(f"Enter Your Answer: ")

#     answers.append(
#         f"{i}. {ans}"
#     )


# # Convert answers list into text
# student_answers = "\n".join(answers)


# # Show collected answers
# print("\nYour Answers:\n")

# print(student_answers)


# # -----------------------------
# # STEP 3: Evaluate Answers
# # -----------------------------

# print("\nEvaluating Answers...\n")

# # Call Evaluation Agent
# feedback = evaluate_answers(
#     json.dumps(questions),
#     student_answers
# )

# # Print feedback
# print("\n=== FEEDBACK ===\n")
# print(feedback)


# # -----------------------------
# # STEP 4: Save Progress
# # -----------------------------

# # Save feedback into JSON file
# save_progress(feedback)