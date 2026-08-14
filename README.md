# RubixLightingControl

RubixLightingControl is a local-first, modular lighting control platform.

## Current milestone

v0.1.0-dev — Foundation

## Initial hardware

- Raspberry Pi 4B
- 4 × Raspberry Pi Pico 2 W
- One Pico 2 W per LED strip
- Existing addressable pixel tape

## Network design

RubixLightingControl uses an existing router.

Internet access is optional.

The controller must continue working on the local network even when the router has no Internet connection.

## Client access

The web interface will be accessible from:

- Computer
- Phone
- Tablet

## Architecture

```text
Phone / Tablet / Computer
          |
      Web Browser
          |
  Raspberry Pi 4B
          |
      Local Router
          |
   Pico 2 W Nodes
          |
      LED Strips