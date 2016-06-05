

#!/usr/bin/python

import subprocess

print "@@@@     This program displays the system health condition    @@@@"

print "!!!!!!!!!!!!!   Users logged in   !!!!!!!!!!!!!!!!!"
subprocess.call('who')

print "!!!!!!!!!!!!!   Memory stats   !!!!!!!!!!!!!!!!!"
subprocess.call(['free', '-m'])

print "!!!!!!!!!!!!!   Disk details  !!!!!!!!!!!!!!!!!"
subprocess.call(['df', '-h'])

print "!!!!!!!!!!!!!   Top processes  !!!!!!!!!!!!!!!!!"
subprocess.call(['top'])

print "#########################"
