**Quiz AI Backend**

An AI-powered quiz generation and evaluation system built with:

FastAPI
LangChain
Ollama
PostgreSQL
SQLAlchemy
Chroma

This project generates quizzes using AI, stores quizzes in PostgreSQL, evaluates user submissions, and is being extended with RAG (Retrieval-Augmented Generation) for quiz creation from user-provided documents.

**Features
Current Features**
AI-generated MCQ quizzes
Quiz storage in PostgreSQL
Answer evaluation
AI mentor feedback
FastAPI REST APIs
LangChain + Ollama integration
JSON validation using Pydantic
RAG foundation using ChromaDB
Tech Stack
Technology	Purpose
Python	Backend language
FastAPI	API framework
PostgreSQL	Database
SQLAlchemy	ORM
LangChain	LLM orchestration
Ollama	Local LLM execution
ChromaDB	Vector database
Pydantic	Validation


**Installation**
1. Clone repository
git clone <your-github-repo-url>
cd quiz-ai
2. Create virtual environment
macOS/Linux
python -m venv .venv
source .venv/bin/activate
Windows
python -m venv .venv
.venv\Scripts\activate
3. Install dependencies
pip install -r requirements.txt
PostgreSQL Setup

**Install**:

PostgreSQL Official Website

Create database:

CREATE DATABASE quiz_ai;

Update database URL inside:

app/db/database.py

**Example**:

DATABASE_URL = "postgresql://username:password@localhost:5432/quiz_ai"
Ollama Setup

**Install**:

Ollama Official Website

Pull model:

ollama pull llama3

Start Ollama:

ollama serve
Run Application
uvicorn app.main:app --reload

API Docs:

http://127.0.0.1:8000/docs
Example APIs
Generate Quiz
POST /quiz

Request:

{
  "topic": "Python",
  "num_questions": 5
}
Submit Quiz
POST /quiz/submit

Request:

{
  "quiz_id": 1,
  "answers": {
    "1": "A",
    "2": "C"
  }
}
RAG (Work in Progress)

Current RAG implementation includes:

Chroma vector database
Embedding generation
Similarity search
Retrieval-based AI responses

Upcoming features:

PDF upload
DOC upload
Quiz generation from uploaded documents
Personalized learning paths
Adaptive quizzes
