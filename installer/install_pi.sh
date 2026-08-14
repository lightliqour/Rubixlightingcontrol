#!/usr/bin/env bash

set -euo pipefail

APP_NAME="RubixLightingControl"

APP_DIR="/opt/rubixlightingcontrol"
CONFIG_DIR="/etc/rubixlightingcontrol"
DATA_DIR="/var/lib/rubixlightingcontrol"
LOG_DIR="/var/log/rubixlightingcontrol"

echo
echo "===================================="
echo " $APP_NAME Installer"
echo "===================================="
echo

if [[ "$(id -u)" -ne 0 ]]; then
    echo "Please run with sudo."
    exit 1
fi

echo "Creating application directories..."

mkdir -p "$APP_DIR"
mkdir -p "$CONFIG_DIR"
mkdir -p "$DATA_DIR"
mkdir -p "$LOG_DIR"

echo
echo "Directories created successfully."
echo
echo "Installer foundation complete."