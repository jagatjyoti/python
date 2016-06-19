#!/usr/bin/python

import paramiko
try:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print "Trying to connect to host ..."
    ssh.connect('192.168.87.128', username='luckee', password='user@1234')
    stdin, stdout, stderr = ssh.exec_command('hostname')
    print "Output: \n", stdout.readlines()
except paramiko.SSHException:
    print "Error: \n", stderr.readlines()
finally:
    ssh.close()
    print "Active SSH connection closed"
