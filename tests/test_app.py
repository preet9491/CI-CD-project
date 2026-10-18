
import pytest
from app import app, students


@pytest.fixture
def client():
    app.config["TESTING"] = True
    students.clear()

    with app.test_client() as test_client:
        yield test_client

    students.clear()


def test_homepage(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Student Registration" in response.data


def test_register_student(client):
    response = client.post("/", data={
        "name": "Rahul",
        "email": "rahul@example.com",
        "course": "BCA"
    })

    assert response.status_code == 200
    assert b"Rahul" in response.data
    assert b"rahul@example.com" in response.data


def test_invalid_course(client):
    response = client.post("/", data={
        "name": "Rahul",
        "email": "rahul@example.com",
        "course": "InvalidCourse"
    })

    assert response.status_code == 200
    assert b"Please enter valid registration details." in response.data
    assert len(students) == 0


def test_health_endpoint(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json == {"status": "healthy"}
