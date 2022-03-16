#!/usr/bin/expect

set prompt ":/"
set path ""
# [e.g.] "/data/local/tmp"
set server ""
# [e.g.] "frida-server-15.1.12-android-arm64" 

eval spawn adb shell
expect $prompt
send "su\r"
expect $prompt
send "cd $path\r"
expect $prompt
send "./$server\r"
interact
