import requests

BASE_URL = "http://localhost:4567"


def test_get_todos():
    response = requests.get(f"{BASE_URL}/todos")
    assert response.status_code == 200
    assert "todos" in response.json()
