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

import httplib, re
from optparse import OptionParser
from time import sleep

class HTTPStatus:
	def __init__(self):
		self.host = ""
		self.path = ""
		self.http_method = ""

		usage = "usage: %prog -m method -t target"
		parser = OptionParser(usage=usage)
		parser.add_option("-m", "--method", dest="method",
				help="HTTP method: GET, POST, PUT, DELETE", metavar="http_method")
		parser.add_option("-t", "--target", dest="target",
				help="Your target host", metavar="target_host")
		(opts, args) = parser.parse_args()

		if opts.target:
			self.host = opts.target

			if re.search("http://", self.host):
				self.host = self.host.split("http://", 1)
				self.host = self.host[1]

			# extract hostname & path
			try:
				self.host = self.host.split("/", 1)
				self.path = "/"+self.host[1]
				self.host = self.host[0]
			except:
				self.host = self.host[0]
				self.path = "/"

		if opts.method:
			self.http_method = opts.method

	def getTarget(self):
		return self.host+self.path

	def getHTTPMethod(self):
		method_name = ""
		if re.match("(GET|POST|PUT|DELETE)", self.http_method):
			method_name = self.http_method
		return method_name

	def sendRequest(self):
		try:
			print "[!] building Connection..."
			conn = httplib.HTTPConnection(self.host)
			sleep(1)
			print "[!] Sending Request..."
			conn.request(self.http_method, self.path)
			sleep(1)
			print "[!] Reading Response...\n"
			resp = conn.getresponse()
			sleep(1)
			print "[+] Summary"
			print "[+] ---------------------------"
			print "[+] Target: http://"+self.host+self.path
			print "[+] Status Code:", resp.status
			print "[+] Status Message:", resp.reason
			print "[+] ---------------------------\n"
			conn.close()
		except:
			print "[-] Error! Check Your Internet Connection and target host."

if __name__ == "__main__":
	print "\n[+] ---------------------------------------------------"
	print "[+] Show HTTP Status Code and HTTP Status Message"
	print "[+] httpstatus.py - slac3dork@gmail.com"
	print "[+] Coded by: slac3dork"
	print "[+] ---------------------------------------------------\n"
	sleep(2)
	obj = HTTPStatus()
	target = obj.getTarget()
	method = obj.getHTTPMethod()
	if target and method:
		obj.sendRequest()

