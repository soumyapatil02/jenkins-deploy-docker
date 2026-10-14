from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_home_returns_success_message():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "Employee Management System is running!",
        "status": "success",
    }


def test_health_check_returns_healthy():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}
