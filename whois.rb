#!/usb/bin/ruby

#  _________      .__       .____   _______
# /   _____/ ____ |__|_____ |    |  \   _  \    ____
# \_____  \ /    \|  \____ \|    |  /  /_\  \  / ___\
# /        \   |  \  |  |_> >    |__\  \_/   \/ /_/  >
#/_______  /___|  /__|   __/|_______ \_____  /\___  /
#        \/     \/   |__|           \/     \//_____/
# http://snippet.c0de.me
# slac3dork[at]gmail[dot]com
#
# Special Thanks to Beenu Aurora for the inspiration.

require 'open-uri'

if ARGV.size < 1
puts '[-] Usage ./whois.rb <domain_name>'
exit 1
end

puts '-----------------------------------------------'
puts '[+] Whois tool - whois.rb'
puts '[+] Thanks to Beenu'
puts '[+] Author: slac3dork'
puts "-----------------------------------------------\n\n"

begin
	domain_name = ARGV[0]
	open("http://reports.internic.net/cgi/whois?whois_nic=#{domain_name}&type=domain") {|page|
	    page.each_line {|line|
		    if (line =~ /Domain Name:/)
			    puts "[+]#{line}"
                    end

		    if (line =~ /Registrar:/)
			    puts "[+]#{line}"
                    end

		    if (line =~ /Name Server:/)
			    puts "[+]#{line}"
                    end

		    if (line =~ /Whois Server:/)
			    puts "[+]#{line}"
                    end

		    if (line =~ /Referral URL:/)
			    puts "[+]#{line}"
                    end

		    if (line =~ /Status:/)
			    puts "[+]#{line}"
                    end

		    if (line =~ /Updated Date:/)
			    puts "[+]#{line}"
                    end

		    if (line =~ /Creation Date:/)
			    puts "[+]#{line}"
                    end

		    if (line =~ /Expiration Date:/)
			    puts "[+]#{line}"
                    end
		}
	   }
rescue OpenURI::HTTPError => error_msg
        puts "[-] Ups! Got bad status code: #{error_msg}. Try again."
rescue Timeout::Error
        puts '[-] 0ops! Timeout bro, check your internet connection.'
end

