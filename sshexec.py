#!/usr/bin/python

import paramiko
try:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect('ip=192.168.87.129', username='luckee', password='lucky@123')
    stdin, stdout, stderr = ssh.exec_command('uptime')
    print "Output: \n", stdout.readlines()
except paramiko.SSHException:
    print "Error: \n", stderr.readlines()
finally:
    ssh.close()
    print "Active SSH connection closed"
