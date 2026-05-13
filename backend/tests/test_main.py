"""
Unit tests for the Scholarly FastAPI application.
Tests all CRUD endpoints using a temporary in-memory SQLite database.
"""
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from ..database import Base, get_db
from ..main import app
from ..enums import ResourceStatus

# Setup an in-memory SQLite database for testing
SQLALCHEMY_DATABASE_URL = "sqlite://"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def override_get_db():
    """
    Dependency override to use the testing database session.
    """
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

# Apply the dependency override to the FastAPI app
app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

@pytest.fixture(autouse=True)
def setup_database():
    """
    Create tables before each test and drop them after.
    """
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

def test_create_resource():
    """
    Test creating a new research resource.
    """
    response = client.post(
        "/resources/",
        json={
            "title": "Test Paper",
            "link": "http://example.com",
            "category": "Testing",
            "status": "Pending"
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test Paper"
    assert data["category"] == "Testing"
    assert "id" in data

def test_read_resources():
    """
    Test retrieving a list of resources.
    """
    # Create one resource first
    client.post(
        "/resources/",
        json={"title": "Paper 1", "link": "http://p1.com", "category": "A"}
    )
    
    response = client.get("/resources/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["title"] == "Paper 1"

def test_update_resource():
    """
    Test updating an existing resource.
    """
    # Create
    create_resp = client.post(
        "/resources/",
        json={"title": "Old Title", "link": "http://old.com", "category": "Old"}
    )
    resource_id = create_resp.json()["id"]
    
    # Update
    update_resp = client.put(
        f"/resources/{resource_id}",
        json={"title": "New Title", "status": "Completed"}
    )
    assert update_resp.status_code == 200
    data = update_resp.json()
    assert data["title"] == "New Title"
    assert data["status"] == "Completed"

def test_delete_resource():
    """
    Test deleting a resource.
    """
    # Create
    create_resp = client.post(
        "/resources/",
        json={"title": "To Delete", "link": "http://del.com", "category": "D"}
    )
    resource_id = create_resp.json()["id"]
    
    # Delete
    delete_resp = client.delete(f"/resources/{resource_id}")
    assert delete_resp.status_code == 200
    assert delete_resp.json()["message"] == "Resource deleted successfully"
    
    # Verify deletion
    get_resp = client.get("/resources/")
    assert len(get_resp.json()) == 0

def test_update_non_existent_resource():
    """
    Test updating a resource that doesn't exist.
    """
    response = client.put("/resources/999", json={"title": "Fail"})
    assert response.status_code == 404
    assert response.json()["detail"] == "Resource not found"
