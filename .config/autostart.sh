#!/bin/sh

# systray battery icon
cbatticon -u 5 &
# systray volume
volumeicon &
# Background Configuration
nitrogen --restore
# USB
udiskie -t &
# Transparency Background
picom --experimental-backends &
# Policy Kit Agent
/usr/lib/policykit-1-pantheon/io.elementary.desktop.agent-polkit &