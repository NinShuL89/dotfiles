#!/bin/sh

function run {
  if ! pgrep $1 ;
  then
    $@&
  fi
}

# Screens

run xrandr --output LVDS1 --primary --mode 1366x768 --pos 276x1080 --output HDMI1 --mode 1920x1080 --pos 0x0 &

# LxQt PolicyKit  
/usr/bin/lxqt-policykit-agent &		# Install lxqt-polkit & lxqt-admin

# systray battery icon
run cbatticon -u 5 &
# systray volume
run volumeicon &
#Telegram 
run telegram-desktop &
# Composer
run picom &
# Network
run nm-applet &
# Automount Devices
run udiskie -t &
# Wallpaper
run nitrogen --restore &
# Automount Devices
#run udiskie -t &
#Wallpaper Changer
run variety &