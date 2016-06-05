#!/usr/bin/python

import subprocess
user = 'emc'
cmd = subprocess.Popen(['grep', 'emc', '/etc/passwd'])
if cmd == "":
  print "User trace failed, try again !"

else:
  print "User found !"
  print cmd
