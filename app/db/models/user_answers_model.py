from datetime import datetime
from sqlalchemy import Boolean, Column, DateTime, String, Integer

from app.db.database import Base

class UserAnswer(Base):
    __tablename__ = 'user_answers'
    id = Column(Integer, primary_key=True)
    question_id = Column(Integer)
    selected_answer = Column(String)
    is_correct = Column(Boolean)
    created_at = Column(DateTime, default=datetime.utcnow)