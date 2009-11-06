#!/usr/bin/python
#
#  _________      .__       .____   _______
# /   _____/ ____ |__|_____ |    |  \   _  \    ____
# \_____  \ /    \|  \____ \|    |  /  /_\  \  / ___\
# /        \   |  \  |  |_> >    |__\  \_/   \/ /_/  >
#/_______  /___|  /__|   __/|_______ \_____  /\___  /
#        \/     \/   |__|           \/     \//_____/
# http://snippet.c0de.me
# slac3dork@gmail.com

import urllib2, sys, re
from time import sleep

def serverInfo(server):
	try:
		print "[-]building request"
		req = urllib2.Request(server)
		sleep(2)
		print "[-]sending request"
		url = urllib2.urlopen(req)
		print "[-]getting information...\n"
		server_info = url.info()
		sleep(2)
		return server_info
	except (urllib2.URLError):
		status = "address not found"
		return status

def welcomeBro():
	print "[+] --------------------------------"
	print "[+] Getting HTTP server infomation"
	print "[+] httserverinfo.py"
	print "[+] Coded By slac3dork"
	print "[+] Greetz to low1z"
	print "[+] --------------------------------\n"

def error():
	print "error bro!"
	print "hey, you don't know how to use this?"
	print "usage: python httpserverinfo.py <target>\n"
	print "target example: http://google.com"

if (__name__ == "__main__"):
	welcomeBro()

	if (len(sys.argv) == 2):
		server = sys.argv[1]
		if (not (re.search("http://", server))):
			server = "http://"+server
		print serverInfo(server)
	else:
		error()

