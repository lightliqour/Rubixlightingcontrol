from pathlib import Path
import sys

sys.path.insert(
    0,
    str(Path(__file__).parents[1] / "backend"),
)

from app.config.models import ControllerConfig
from app.config.store import ConfigStore


def test_config_store_creates_default_config(
    tmp_path: Path,
) -> None:
    config_file = tmp_path / "controller.json"

    store = ConfigStore(
        config_file=config_file,
    )

    config = store.load()

    assert config_file.exists()
    assert config.project_name == "RubixLightingControl"
    assert config.controller_name == "Rubix Controller"
    assert config.port == 8000


def test_config_store_round_trip(
    tmp_path: Path,
) -> None:
    config_file = tmp_path / "controller.json"

    store = ConfigStore(
        config_file=config_file,
    )

    original = ControllerConfig(
        controller_name="Test Controller",
        port=9000,
        log_level="DEBUG",
    )

    store.save(original)

    loaded = store.load()

    assert loaded.controller_name == "Test Controller"
    assert loaded.port == 9000
    assert loaded.log_level == "DEBUG"