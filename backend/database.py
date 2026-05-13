"""
Database configuration for the Scholarly application.
Sets up the SQLAlchemy engine, session, and base class.
"""
from sqlalchemy.ext.declarative import declarative_base

# Base class for SQLAlchemy models
Base = declarative_base()
