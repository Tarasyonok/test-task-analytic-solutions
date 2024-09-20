from sqlalchemy import JSON, Column, DateTime, Integer, String
from app.database import Base

class Document(Base):
    __tablename__ = "documents"
    
    id = Column(Integer, primary_key=True)
    text = Column(String)
    created_date = Column(DateTime)
    rubrics = Column(JSON)
