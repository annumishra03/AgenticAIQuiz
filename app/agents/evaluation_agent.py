# Import Ollama wrapper
from langchain_ollama import ChatOllama

# Import prompt template
from langchain_core.prompts import ChatPromptTemplate


# Local model
llm = ChatOllama(
    model="llama3",temperature=0.3
)


# Evaluation prompt
evaluation_prompt = ChatPromptTemplate.from_template(
"""
You are an AI mentor.

Analyze the quiz performance.

Quiz Topic:
{topic}

Results:
{results}

Percentage:
{percentage}

Provide:
1. Performance summary
2. Weak areas
3. Improvement suggestions
4. Recommended next topic

Keep response concise.
"""
)


# Evaluation function
def generate_ai_feedback(topic, result, percentage):

    # Prompt → LLM
    chain = evaluation_prompt | llm

    # Send quiz + answers
    response = chain.invoke({
        "topic": topic,
        "results": result,
        "percentage": percentage
    })

    # Return evaluation
    return response.content