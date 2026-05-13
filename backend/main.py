"""
Main entry point for the Scholarly FastAPI application.
This module initializes the FastAPI app and defines the core routes.
"""
from fastapi import FastAPI

app = FastAPI(title="Scholarly API")

@app.get("/")
def read_root():
    """
    Root endpoint that returns a welcome message.
    """
    return {"message": "Hello from Scholarly API"}
