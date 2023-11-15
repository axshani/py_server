from fastapi import FastAPI
from fastapi.testclient import TestClient

app = FastAPI()
client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}


def test_add_event():
    e = {
            "name": "Birthday",
            "date": "2022-12-27",
            "location": "Yuma",
            "tags": ["outdoor"],
            "time": "15:00",
            "number_of_participants": 15
        }

    response = client.post("/events", data=e)
    assert response.status_code == 200
    assert response.json()["name"] == e["name"]
