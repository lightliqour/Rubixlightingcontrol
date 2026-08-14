import sys
from pathlib import Path

sys.path.insert(
    0,
    str(Path(__file__).parents[1] / "backend"),
)

from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_system_status() -> None:
    response = client.get("/api/v1/system/status")

    assert response.status_code == 200

    body = response.json()

    assert body["project"] == "RubixLightingControl"
    assert body["version"] == "0.1.0-dev"
    assert body["status"] == "online"