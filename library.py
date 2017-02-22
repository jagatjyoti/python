#!/usr/bin/python
 
import paramiko
import socket
import sys
 
 
def set_connection():
 
  try:
 
     s = paramiko.SSHClient()
     s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
     print "Trying to connect to host ..."
     s.connect('192.168.87.130', username='luckee', password='lucky@123')
     print "Connection Established !!"
 
  except KeyboardInterrupt:
     print "Ctrl + C pressed. Aborting ..."
     sys.exit()
 
  except socket.gaierror:
     print "Name resolution of remote host failed. Exiting ..."
     sys.exit()
 
  except socket.error:
     print "Couldn't connect to remote server. Exiting ..."
     sys.exit()
  return s
 
def connection_close(Fd):
  Fd.close()
 
 
def exec_command(cmd):
 
  ssh_fd=set_connection()
  stdin, stdout, stderr = ssh_fd.exec_command(cmd)
  print "---------Result--------"
 
  e=stderr.readlines()
  if len(e) != 0:
     print "Error in running command !"
     print e
 
  
  if any("Reason" in s for s in stdout.readlines()):
     print "No such service !!"
 
  if any("Inactive" or "Dead" in s for s in stdout.readlines()):
     print "Service is down !!"
 
  if any("running" in s for s in stdout.readlines()):
     print "Service is up !!"