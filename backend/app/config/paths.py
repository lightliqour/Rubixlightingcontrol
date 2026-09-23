from dataclasses import dataclass
from pathlib import Path
import os


@dataclass(frozen=True)
class RuntimePaths:
    config_dir: Path
    data_dir: Path
    log_dir: Path


def load_runtime_paths() -> RuntimePaths:
    if os.name == "nt":
        base_dir = Path.cwd() / "runtime"

        return RuntimePaths(
            config_dir=base_dir / "config",
            data_dir=base_dir / "data",
            log_dir=base_dir / "logs",
        )

    return RuntimePaths(
        config_dir=Path(
            os.getenv(
                "RUBIX_CONFIG_DIR",
                "/etc/rubixlightingcontrol",
            )
        ),
        data_dir=Path(
            os.getenv(
                "RUBIX_DATA_DIR",
                "/var/lib/rubixlightingcontrol",
            )
        ),
        log_dir=Path(
            os.getenv(
                "RUBIX_LOG_DIR",
                "/var/log/rubixlightingcontrol",
            )
        ),
    )


runtime_paths = load_runtime_paths()