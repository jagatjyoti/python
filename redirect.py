#!/usr/bin/python

import subprocess

sp = subprocess.Popen(['ls', '-l'], stdout=subprocess.PIPE)
output, _ = sp.communicate()
print "Status:", sp.wait()
print "Outut:" 
print output
