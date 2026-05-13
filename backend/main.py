"""
Main entry point for the Scholarly FastAPI application.
This module initializes the FastAPI app and defines the core routes.
"""
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from . import models, schemas, database
from .database import engine, get_db

# Create the database tables on startup
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Scholarly API")

@app.get("/")
def read_root():
    """
    Root endpoint that returns a welcome message.
    """
    return {"message": "Hello from Scholarly API"}

@app.post("/resources/", response_model=schemas.Resource)
def create_resource(resource: schemas.ResourceCreate, db: Session = Depends(get_db)):
    """
    Create a new research resource in the database.
    """
    db_resource = models.Resource(
        title=resource.title,
        link=resource.link,
        category=resource.category,
        status=resource.status
    )
    db.add(db_resource)
    db.commit()
    db.refresh(db_resource)
    return db_resource

@app.get("/resources/", response_model=List[schemas.Resource])
def read_resources(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Retrieve a list of research resources from the database.
    Supports pagination via 'skip' and 'limit'.
    """
    resources = db.query(models.Resource).offset(skip).limit(limit).all()
    return resources
