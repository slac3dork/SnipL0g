#!/usr/bin/python

#  _________      .__       .____   _______
# /   _____/ ____ |__|_____ |    |  \   _  \    ____
# \_____  \ /    \|  \____ \|    |  /  /_\  \  / ___\
# /        \   |  \  |  |_> >    |__\  \_/   \/ /_/  >
#/_______  /___|  /__|   __/|_______ \_____  /\___  /
#        \/     \/   |__|           \/     \//_____/
# http://snippet.c0de.me
# slac3dork@gmail.com

import sys
import socket
import threading

class Scanner(threading.Thread):
	def __init__(self, host, port):
		threading.Thread.__init__(self)
		self.host = host
		self.port = port
		self.status = ""

	def run(self):
		self.sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sk.settimeout(0.03)
		try:
			self.sk.connect((self.host, self.port))
		except:
			pass
		else:
			self.status = "open"
			self.sk.close()

def error():
	print "Usage: ./portScanner.py <target> <startport> <endport>"

def welcomeMsg():
	print "---------------------------------------------"
	print " portScanner.py - A Simple Port Scanner Tool"
	print " coded by slac3dork"
	print "---------------------------------------------"

if (__name__ == "__main__"):
	if (len(sys.argv) != 4):
		error()
	else:
		welcomeMsg()

		target = sys.argv[1]
		startPort = int(sys.argv[2])
		endPort = int(sys.argv[3])
		threads = []
		for port in range(startPort, endPort):
			thread = Scanner(target, port)
			threads.append(thread)
			thread.start()

		print "Target = ", target

		for thread in threads:
			if (thread.status == "open"):
				print "Port", thread.port, " : ", thread.status
