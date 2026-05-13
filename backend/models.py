"""
Database models for the Scholarly application.
Uses SQLAlchemy to define the structure of the research resources table.
"""
from sqlalchemy import Column, Integer, String
from .database import Base
from .enums import ResourceStatus

class Resource(Base):
    """
    SQLAlchemy model for the 'resources' table.
    Tracks academic resources like papers, links, and study notes.
    """
    __tablename__ = "resources"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    link = Column(String)
    category = Column(String, index=True)
    status = Column(String, default=ResourceStatus.PENDING)
