from urllib import response

import requests

BASE_URL ="https://jsonplaceholder.typicode.com"

def test_get_user():
    response = requests.get(f"{BASE_URL}/users/1",
                            timeout=10)
assert response.status_code == 200
data = response.json()
assert data["id"] ==1
assert "name" in data
assert "email" in data