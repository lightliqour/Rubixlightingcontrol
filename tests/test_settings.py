from pathlib import Path
import sys

sys.path.insert(
    0,
    str(Path(__file__).parents[1] / "backend"),
)

from fastapi.testclient import TestClient

from app.api.v1 import settings as settings_api
from app.config.store import ConfigStore
from app.main import app


client = TestClient(app)


def test_get_settings(
    tmp_path: Path,
    monkeypatch,
) -> None:
    test_store = ConfigStore(
        config_file=tmp_path / "controller.json",
    )

    monkeypatch.setattr(
        settings_api,
        "config_store",
        test_store,
    )

    response = client.get(
        "/api/v1/settings/",
    )

    assert response.status_code == 200

    body = response.json()

    assert body["project_name"] == "RubixLightingControl"
    assert body["version"] == "0.1.0-dev"
    assert body["port"] == 8000


def test_update_settings(
    tmp_path: Path,
    monkeypatch,
) -> None:
    test_store = ConfigStore(
        config_file=tmp_path / "controller.json",
    )

    monkeypatch.setattr(
        settings_api,
        "config_store",
        test_store,
    )

    payload = {
        "project_name": "RubixLightingControl",
        "controller_name": "Test Controller",
        "version": "0.1.0-dev",
        "host": "0.0.0.0",
        "port": 8100,
        "log_level": "DEBUG",
    }

    response = client.put(
        "/api/v1/settings/",
        json=payload,
    )

    assert response.status_code == 200

    body = response.json()

    assert body["controller_name"] == "Test Controller"
    assert body["port"] == 8100
    assert body["log_level"] == "DEBUG"

    saved = test_store.load()

    assert saved.controller_name == "Test Controller"
    assert saved.port == 8100