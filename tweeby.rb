#!/usb/bin/ruby

#  _________      .__       .____   _______
# /   _____/ ____ |__|_____ |    |  \   _  \    ____
# \_____  \ /    \|  \____ \|    |  /  /_\  \  / ___\
# /        \   |  \  |  |_> >    |__\  \_/   \/ /_/  >
#/_______  /___|  /__|   __/|_______ \_____  /\___  /
#        \/     \/   |__|           \/     \//_____/
# http://snippet.c0de.me
# slac3dork[at]gmail[dot]com

require 'optparse'
require 'net/http'

class Tweeby

        def initialize
                puts '-------------------------------------------------------'
                puts '[+] Tweeby - cURL alternative to update twitter status'
                puts '[+] Tweeby.rb - http://snippet.c0de.me'
                puts '[+] Author: slac3dork'
                puts "-------------------------------------------------------\n\n"
        end

        def parseOptions
                begin
                        options = {}
                        opts = OptionParser.new
                        opts.banner = "Usage: ./tweeby.rb -u your_username -p your_password -s your_status\nExample: ./tweeby.rb -u myuser -p mypassword -s 'this is my status'"
                        opts.on('-u your_username', '--user your_username', 'your_username = Your Twitter username') do |u|
                                @username = u
                        end
                        opts.on('-p your_password', '--password your_password', 'your_password = Your Twitter password') do |p|
                                @passwd = p
                        end
                        opts.on('-s your_status', '--status your_status', 'your_status = Your Twitter status message') do |s|
                                @status = s
                        end
                        opts.on('-v', '--verbose', 'Run verbosely') do |v|
                                @verbose = v
                        end
                        opts.parse!

                        if (!(@username and @passwd and @status))
                                puts opts
                                exit(1)
                        end

                rescue OptionParser::ParseError
                       puts opts
                       exit(1)
                end
        end

        def sendTweet
                begin
                        puts '[+] Starting Tweeby...'
                        tweet = Net::HTTP.post_form(
                                URI.parse("http://#{@username}:#{@passwd}@twitter.com/statuses/update.xml"),
                                {"status"=>"#{@status}"})

                        if @verbose
                                puts tweet.body
                        else
                                puts '[+] Your status has been updated'
                        end
                        puts '[+] Done...'

                rescue Exception
                        puts '[-] Error while tweeting, check your username, password, and internet connection'
                end
        end

end
# main
twitter = Tweeby.new
twitter.parseOptions
twitter.sendTweet

