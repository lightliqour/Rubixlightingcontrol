from dataclasses import asdict, dataclass


@dataclass
class ControllerConfig:
    project_name: str = "RubixLightingControl"
    controller_name: str = "Rubix Controller"
    version: str = "0.1.0-dev"
    host: str = "0.0.0.0"
    port: int = 8000
    log_level: str = "INFO"

    def to_dict(self) -> dict[str, object]:
        return asdict(self)

    @classmethod
    def from_dict(
        cls,
        data: dict[str, object],
    ) -> "ControllerConfig":
        return cls(
            project_name=str(
                data.get(
                    "project_name",
                    "RubixLightingControl",
                )
            ),
            controller_name=str(
                data.get(
                    "controller_name",
                    "Rubix Controller",
                )
            ),
            version=str(
                data.get(
                    "version",
                    "0.1.0-dev",
                )
            ),
            host=str(
                data.get(
                    "host",
                    "0.0.0.0",
                )
            ),
            port=int(
                data.get(
                    "port",
                    8000,
                )
            ),
            log_level=str(
                data.get(
                    "log_level",
                    "INFO",
                )
            ),
        )