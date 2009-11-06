#!/bin/bash
#
#  _________      .__       .____   _______
# /   _____/ ____ |__|_____ |    |  \   _  \    ____
# \_____  \ /    \|  \____ \|    |  /  /_\  \  / ___\
# /        \   |  \  |  |_> >    |__\  \_/   \/ /_/  >
#/_______  /___|  /__|   __/|_______ \_____  /\___  /
#        \/     \/   |__|           \/     \//_____/
# http://snippet.c0de.me
# slac3dork@gmail.com

clear
echo '-----------------------------------------------------------'
echo 'simple bash script to show computer specification'
echo 'slac3dork[at]gmail[dot]com - http://snippet.c0de.me'
echo '-----------------------------------------------------------'
echo
user_id=`id -u`

if [ $user_id -ne 0 ]; then
  echo "Only root can run this script"
  exit
fi

echo === Computer Spesification ===
echo

# MAIN SPECIFICATION

# ========== PROSESOR ==========
core=`cat /proc/cpuinfo | grep -c "model name"`
model=`cat /proc/cpuinfo | grep "model name" | head -n1 | cut -f2 -d ":"`
cache=`cat /proc/cpuinfo | grep cache | head -n1 | cut -f2 -d ":"`

echo PROCESSOR
echo core" = $core"
echo model" = $model"
echo cache size" = $cache"
echo

# ========== RAM =========
memTotal=`cat /proc/meminfo | head -n1 | cut -f8 -d " "`
memTotalMB=`expr $memTotal / 1024`

echo RAM / Main Memory
echo Total Memory" = $memTotal KB = $memTotalMB MB"
echo

# ========== Harddisk =========
hdTotal=`cat /proc/partitions | head -n3 | tail -n1 | cut -f12 -d " "`
hdTotalMB=`expr $hdTotal / 1024`
hdTotalGB=`expr $hdTotalMB / 1024`

echo Harddisk
echo Total Capacity" = $hdTotalMB MB = $hdTotalGB GB"
echo

# ========== VGA ==========
vga=`lspci | grep VGA | cut -f3 -d":"`

echo VGA / Graphic Card
echo Model" = $vga"
echo

# ADDITIONAL Specification

# ========== AUDIO ==========
audio=`lspci | grep Audio | cut -f3 -d":"`

echo Audio
echo Model" = $audio"
echo

# ========== Ethernet ==========
eth=`lspci | grep Ethernet | cut -f3 -d":"`

echo Ethernet / LAN Card
echo Model" = $eth"
echo
echo

echo "Thanks for using this script. By slac3dork"

