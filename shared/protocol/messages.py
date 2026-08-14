from dataclasses import dataclass


@dataclass(frozen=True)
class DiscoveryMessage:
    node_id: str
    node_type: str
    firmware_version: str
    protocol_version: int


@dataclass(frozen=True)
class StatusMessage:
    node_id: str
    status: str
    uptime_seconds: int


@dataclass(frozen=True)
class ConfigMessage:
    node_id: str
    output_id: str
    led_type: str
    pixel_count: int
    brightness_limit: float


@dataclass(frozen=True)
class FrameMessage:
    node_id: str
    output_id: str
    sequence: int
    payload: bytes