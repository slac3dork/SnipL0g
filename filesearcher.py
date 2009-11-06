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

def searching(dir, target):
        status = False
        for rootdir, dirs, files in walk(dir):
                for file in files:
                        if file == target:
                                status = True
                                path = rootdir+"/"
        if status:
                print target, "was found at:", path
        else:
                print target, "not found"

if __name__ == "__main__":
        if len(argv) != 2:
                print "Usage: python filesearcher.py <TARGET_DIR>"
                exit()

        filename = raw_input("target file: ")
        dir_name = argv[1]
        searching(dir_name, filename)

