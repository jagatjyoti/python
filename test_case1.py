#!/usr/bin/python

from library import *

cmd = 'systemctl status network'
print "========================================"
print "           Checking service             "
print "========================================"
exec_command(cmd)