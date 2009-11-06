#!/usb/bin/ruby

#  _________      .__       .____   _______
# /   _____/ ____ |__|_____ |    |  \   _  \    ____
# \_____  \ /    \|  \____ \|    |  /  /_\  \  / ___\
# /        \   |  \  |  |_> >    |__\  \_/   \/ /_/  >
#/_______  /___|  /__|   __/|_______ \_____  /\___  /
#        \/     \/   |__|           \/     \//_____/
# http://snippet.c0de.me
# slac3dork@gmail.com

def fact(n)
	if n == 0
		1
	else
		n * fact(n-1)
	end
end
print "factorial.rb - Get Factorial value\n"
print "usage: ./factorial.rb <your_value>\n"
print "Coded By slac3dork\n\n"
print "Factorial Value of ",ARGV[0].to_i," = ",fact(ARGV[0].to_i), "\n"
