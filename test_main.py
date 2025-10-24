from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_item():
    response = client.post("/items", json={"id": 1, "name": "Laptop", "price": 2000})
    assert response.status_code == 200
    assert response.json()["name"] == "Laptop"

def test_get_items():
    response = client.get("/items")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_item_not_found():
    response = client.get("/items/99")
    assert response.status_code == 404

def test_update_item():
    client.post("/items", json={"id": 2, "name": "Mouse", "price": 50})
    response = client.put("/items/2", json={"id": 2, "name": "Mouse Pro", "price": 80, "available": False})
    assert response.status_code == 200
    assert response.json()["name"] == "Mouse Pro"

def test_delete_item():
    client.post("/items", json={"id": 3, "name": "Keyboard", "price": 100})
    response = client.delete("/items/3")
    assert response.status_code == 200
    assert response.json()["message"] == "Item deleted successfully"
