import json
from pathlib import Path

from app.config.models import ControllerConfig
from app.config.paths import runtime_paths


class ConfigStore:
    def __init__(
        self,
        config_file: Path | None = None,
    ) -> None:
        self.config_file = config_file or (
            runtime_paths.config_dir / "controller.json"
        )

    def ensure_directory(self) -> None:
        self.config_file.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

    def load(self) -> ControllerConfig:
        if not self.config_file.exists():
            config = ControllerConfig()
            self.save(config)
            return config

        with self.config_file.open(
            "r",
            encoding="utf-8",
        ) as handle:
            data = json.load(handle)

        if not isinstance(data, dict):
            raise ValueError(
                "Controller configuration must be a JSON object."
            )

        return ControllerConfig.from_dict(data)

    def save(
        self,
        config: ControllerConfig,
    ) -> None:
        self.ensure_directory()

        temporary_file = self.config_file.with_suffix(
            ".tmp"
        )

        with temporary_file.open(
            "w",
            encoding="utf-8",
        ) as handle:
            json.dump(
                config.to_dict(),
                handle,
                indent=2,
            )
            handle.write("\n")

        temporary_file.replace(
            self.config_file
        )


config_store = ConfigStore()