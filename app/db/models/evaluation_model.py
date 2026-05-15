from datetime import datetime
from sqlalchemy import JSON, Column, DateTime, Float, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base

class Evaluation(Base):
    __tablename__ = 'evaluation'
    id = Column(Integer, primary_key=True, index=True)
    quiz_id = Column(Integer, ForeignKey("quizzes.id"))
    score = Column(Integer, nullable=False)
    percentage = Column(Float, nullable=False)
    feedback = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
