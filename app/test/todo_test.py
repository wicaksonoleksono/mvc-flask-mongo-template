import json
import pytest


def test_get_todos(client):
    """Test retrieving all todos."""
    response = client.get("/todo")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert isinstance(data, list)
    assert all(todo.get("title") for todo in data)


def test_get_todo_by_id(client):
    """Test retrieving a todo by its ID."""
    # Insert a dummy todo item first
    dummy_todo = {"title": "Test Todo", "description": "This is a test todo"}
    response = client.post("/todo", json=dummy_todo)
    assert response.status_code == 200

    todo_id = response.json.get("id")
    response = client.get(f"/todo/{todo_id}")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data["title"] == dummy_todo["title"]


def test_create_todo(client):
    """Test creating a new todo."""
    dummy_todo = {"title": "Test Todo", "description": "This is a test todo"}
    response = client.post("/todo", json=dummy_todo)
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data["message"] == f"Successfully added {dummy_todo['title']}"
    assert data["id"]


def test_update_todo(client):
    """Test updating an existing todo."""
    # First create a todo to update
    dummy_todo = {"title": "Test Todo", "description": "This is a test todo"}
    response = client.post("/todo", json=dummy_todo)
    assert response.status_code == 200

    todo_id = response.json.get("id")

    # Now update the created todo
    update_data = {
        "title": "Updated Todo",
        "description": "Updated description",
        "completed": True,
    }
    response = client.put(f"/todo/{todo_id}", json=update_data)
    assert response.status_code == 200
    assert response.json["message"] == f"updated no. {todo_id}"


def test_delete_todo(client):
    """Test deleting a todo."""
    # First create a todo to delete
    dummy_todo = {"title": "Test Todo", "description": "This is a test todo"}
    response = client.post("/todo", json=dummy_todo)
    assert response.status_code == 200

    todo_id = response.json.get("id")

    # Now delete the created todo
    response = client.delete(f"/todo/{todo_id}")
    assert response.status_code == 200
    assert response.json["message"] == f"Successfully deleted {todo_id}"
