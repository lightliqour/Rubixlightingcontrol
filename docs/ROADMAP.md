# RubixLightingControl Roadmap

## Current version

v0.1.0-dev

## Current sprint

### Sprint 1 — Foundation

Status: In progress

Goals:

- Repository structure
- FastAPI backend
- Versioned API
- Configuration foundation
- Logging foundation
- WebSocket foundation
- Shared node protocol
- Project documentation
- Raspberry Pi installer foundation
- Automated tests
- GitHub Actions

---

## Sprint 2 — Configuration and persistence

Planned:

- Central configuration manager
- Persistent controller settings
- Runtime paths
- Structured logging
- Environment configuration
- Settings API

---

## Sprint 3 — Database

Planned:

- SQLite database
- Controller records
- Node records
- Output records
- Database migrations

---

## Sprint 4 — Node discovery

Planned:

- Pico 2 W discovery protocol
- Node heartbeat
- Online/offline tracking
- Automatic registration
- Controller discovery service

---

## Sprint 5 — Node communication

Planned:

- Configuration transport
- Status transport
- Frame transport
- Sequence tracking
- Network diagnostics

---

## Sprint 6 — LED output

Planned:

- Pico 2 W LED driver
- Configurable pixel count
- Configurable chipset
- Configurable color order
- Static RGB/RGBW control
- Brightness limiting

Initial chipset targets:

- WS2812B
- SK6812
- WS2815
- APA106
- GS8208

---

## Sprint 7 — Effects engine

Planned:

- Static color
- Rainbow
- Chase
- Pulse
- Twinkle
- Additional effects
- Synchronized multi-node playback

---

## Future

- Square layout engine
- Scenes
- Presets
- Scheduling
- Progressive Web App
- OTA node updates
- Art-Net
- sACN
- DMX
- Additional node hardware