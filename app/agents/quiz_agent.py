# Import Ollama LLM wrapper
import json
from langchain_ollama import ChatOllama

# Import prompt template
from langchain_core.prompts import ChatPromptTemplate

# Create local Ollama model
# This runs completely on your machine
llm = ChatOllama(
    model="llama3",
    format="json"
)


# Prompt template
quiz_prompt = ChatPromptTemplate.from_template("""
You are a strict JSON quiz generator.

Generate {no_of_questions} MCQ questions.

Return ONLY valid JSON.

Format:
[
  {{
    "question": "...",
    "options": [
      "A) ...",
      "B) ...",
      "C) ...",
      "D) ..."
    ],
    "answer": "A"
  }}
]

Topic:
{module_content}
""")



# Quiz generation function
def generate_quiz(module_content, no_of_questions):

    # Create chain:
    # Prompt → LLM
    chain = quiz_prompt | llm

    # Send module content into chain
    response = chain.invoke({
        "module_content": module_content,
        "no_of_questions": no_of_questions
    })
    
    # Return AI response
    return response.content