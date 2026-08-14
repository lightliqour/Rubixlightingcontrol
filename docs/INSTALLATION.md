# Installation

RubixLightingControl is intended to run natively on a dedicated Raspberry Pi 4B.

## Operating environment

Target:

- Raspberry Pi 4B
- Raspberry Pi OS
- Native Python virtual environment
- systemd service

## Planned production paths

Application files:

```text
/opt/rubixlightingcontrol/
```

Configuration:

```text
/etc/rubixlightingcontrol/
```

Runtime data:

```text
/var/lib/rubixlightingcontrol/
```

Logs:

```text
/var/log/rubixlightingcontrol/
```

## Network

The Raspberry Pi connects to an existing router.

The router does not require Internet access for normal RubixLightingControl operation.

## Installer

A native installation script will be added under:

```text
installer/install_pi.sh
```

The installer will eventually:

- Install required system packages
- Create the Python virtual environment
- Install backend dependencies
- Create runtime directories
- Register the RubixLightingControl systemd service
- Enable automatic startup