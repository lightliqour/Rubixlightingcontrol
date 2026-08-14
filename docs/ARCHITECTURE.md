# Architecture

RubixLightingControl uses a controller-and-node architecture.

## Controller

The Raspberry Pi 4B is the central controller.

Its responsibilities include:

- Hosting the web interface
- Storing configuration
- Managing nodes
- Generating lighting effects
- Scheduling
- Layout management
- Future support for additional lighting protocols

## Nodes

A node is a networked hardware device responsible for driving one or more outputs.

The initial node target is the Raspberry Pi Pico 2 W.

For the first installation, each LED strip will use one Pico 2 W.

## Outputs

A node exposes one or more outputs.

An output represents a controllable lighting endpoint.

Examples may eventually include:

- Addressable LED strip
- DMX universe
- Relay output
- Future lighting hardware

The controller should interact with outputs through defined interfaces instead of depending on specific hardware implementations.

## Clients

The web interface must work from:

- Desktop computers
- Phones
- Tablets

The frontend is intended to evolve into a Progressive Web App.

## Local-first design

RubixLightingControl must continue functioning when the local router has no Internet connection.

Normal operation must not depend on cloud services.