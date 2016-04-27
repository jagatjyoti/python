#!/usr/bin/python
 
import os
import socket
 
s = socket.socket()
hostname = '127.0.0.1'
port = 22
response = os.system("ping -c 1 " + hostname)
 
if response == 0:
        try:
                print "Host is up, trying to open socket...\n"
                s.connect((hostname, port))
                print "-----------------"
        except Exception, e:
                print("something's wrong with %s:%d. Exception is %s" % (hostname, port, e))
else:
  print "Host is down."
 
print "Closing socket connection."
s.close()
