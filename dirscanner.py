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

from os import walk
from sys import argv

def scanning(dir):
        for rootdir, dirs, files in walk(dir):
                for file in files:
                        print rootdir+"/"+file

if __name__ == "__main__":
        if len(argv) != 2:
                print "Usage: python dirscanner.py <YOUR_DIR>"
                exit()
        dir_name = argv[1]
        scanning(dir_name)

