from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "healthy"

def test_create_task():
    r = client.post("/tasks/", json={"title": "Test Task", "description": "test"})
    assert r.status_code == 201
    assert r.json()["title"] == "Test Task"

def test_get_tasks():
    r = client.get("/tasks/")
    assert r.status_code == 200
    assert isinstance(r.json(), list)

def test_task_not_found():
    r = client.get("/tasks/99999")
    assert r.status_code == 404
