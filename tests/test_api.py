from fastapi.testclient import TestClient
from unittest.mock import patch
from api.main import app

client = TestClient(app)


@patch("api.main.r")
def test_create_job(mock_redis):
    mock_redis.lpush.return_value = 1
    mock_redis.hset.return_value = 1

    res = client.post("/jobs")
    assert res.status_code == 200
    assert "job_id" in res.json()


@patch("api.main.r")
def test_get_job(mock_redis):
    mock_redis.hget.return_value = b"completed"

    res = client.get("/jobs/test")
    assert res.status_code == 200
    assert res.json()["status"] == "completed"


@patch("api.main.r")
def test_not_found(mock_redis):
    mock_redis.hget.return_value = None

    res = client.get("/jobs/test")
    assert "error" in res.json()
