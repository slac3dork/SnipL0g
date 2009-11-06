#!/usr/bin/python
#
#  _________      .__       .____   _______
# /   _____/ ____ |__|_____ |    |  \   _  \    ____
# \_____  \ /    \|  \____ \|    |  /  /_\  \  / ___\
# /        \   |  \  |  |_> >    |__\  \_/   \/ /_/  >
#/_______  /___|  /__|   __/|_______ \_____  /\___  /
#        \/     \/   |__|           \/     \//_____/
# http://snippet.c0de.me
# slac3dork[at]gmail[dot]com  

import socket 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 3000))
print s.recv(1024) # up to 1024 bytes

