from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .database import Base

class Blog(Base):

    __tablename__ = "blogs"

    id = Column(Integer, primary_key=True, index=True) 
    tittle = Column(String)
    body = Column(String)
    is_active = Column(Boolean, default=True)