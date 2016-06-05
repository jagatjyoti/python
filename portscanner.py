#!/usr/bin/python

import subprocess
import socket
import sys
import os
from datetime import datetime

remote_server = raw_input("Please enter remote host to scan ports: ")
remote_serverIP = socket.gethostbyname(remote_server)

response = os.system("ping -c 1 " + remote_server)
if response != 0:
  print "Remote server is down. Aborting ..."
  sys.exit()
else: 
  print "Remote server is up. Continuing ..."

print "**" *30
print "Scanning ports for remote server ", remote_serverIP
print "**" *30

startime = datetime.now()

try:
    for port in range(1,1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remote_serverIP,port))
        if result == 0:
            print ("Port {}: Open".format(port))
            sock.close()

except KeyboardInterrupt:
    print "Ctrl + C pressed. Aborting ..."
    sys.exit()

except socket.gaierror:
    print "Name resolution of remote host failed. Exiting ..."
    sys.exit()

except socket.error:
    print "Couldn't connect to remote server. Exiting ..."
    sys.exit()

endtime = datetime.now()
total = endtime - startime
print "Port scanning completed in %d seconds" % (total)
