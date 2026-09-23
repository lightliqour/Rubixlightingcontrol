from dataclasses import dataclass
from pathlib import Path
import os


@dataclass(frozen=True)
class RuntimePaths:
    config_dir: Path
    data_dir: Path
    log_dir: Path


def load_runtime_paths() -> RuntimePaths:
    config_dir = os.getenv("RUBIX_CONFIG_DIR")
    data_dir = os.getenv("RUBIX_DATA_DIR")
    log_dir = os.getenv("RUBIX_LOG_DIR")

    if config_dir and data_dir and log_dir:
        return RuntimePaths(
            config_dir=Path(config_dir),
            data_dir=Path(data_dir),
            log_dir=Path(log_dir),
        )

    if os.name == "nt":
        base_dir = Path.cwd() / "runtime"

        return RuntimePaths(
            config_dir=Path(
                config_dir
                or base_dir / "config"
            ),
            data_dir=Path(
                data_dir
                or base_dir / "data"
            ),
            log_dir=Path(
                log_dir
                or base_dir / "logs"
            ),
        )

    return RuntimePaths(
        config_dir=Path(
            config_dir
            or "/etc/rubixlightingcontrol"
        ),
        data_dir=Path(
            data_dir
            or "/var/lib/rubixlightingcontrol"
        ),
        log_dir=Path(
            log_dir
            or "/var/log/rubixlightingcontrol"
        ),
    )


runtime_paths = load_runtime_paths()