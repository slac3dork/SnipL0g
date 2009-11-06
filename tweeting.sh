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

username="YOUR_TWITTER_USERNAME"
password="YOUR_TWITTER_PASSWORD"
tweet=$1

length=`echo $tweet | wc -m`
if [ $length -gt 140 ]; then
        echo "Your tweet is longer than 140 characters"
else
        xml=`curl -k -u $username:$password -d status="$tweet" https://twitter.com/statuses/update.xml`
        echo "$xml"
fi

