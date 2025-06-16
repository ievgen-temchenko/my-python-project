import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to my FastAPI project!", "status": "healthy"}

def test_get_items():
    response = client.get("/api/v1/items/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 0

def test_get_item():
    response = client.get("/api/v1/items/1")
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert "name" in data

def test_create_item():
    new_item = {
        "name": "Test Item",
        "description": "A test item",
        "price": 19.99,
        "is_available": True
    }
    response = client.post("/api/v1/items/", json=new_item)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == new_item["name"]
    assert "id" in data
