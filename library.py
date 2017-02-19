#!/usr/bin/python

import paramiko 
import socket
import sys

global ssh 

def set_connection():

  try:

     ssh = paramiko.SSHClient()
     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
     print "Trying to connect to host ..."
     ssh.connect('192.168.87.129', username='luckee', password='lucky@123')
     
  except KeyboardInterrupt:
    print "Ctrl + C pressed. Aborting ..."
    sys.exit()

  except socket.gaierror:
    print "Name resolution of remote host failed. Exiting ..."
    sys.exit()

  except socket.error:
    print "Couldn't connect to remote server. Exiting ..."
    sys.exit()

  #finally:
   #  ssh.close()
    # print "Active SSH connection closed"


def exec_command(cmd):

  set_connection() 
  stdin, stdout, stderr = ssh.exec_command(cmd)
  print "Output: \n", stdout.readlines()
     
  if len(stderr) != 0:
     print "Error in running command !"
     print stderr.readlines() 
