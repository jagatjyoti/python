#!/usr/bin/python

import paramiko
try:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
<<<<<<< HEAD
    ssh.connect('ip=192.168.87.129', username='luckee', password='lucky@123')
=======
    ssh.connect('ip=192.168.87.128', username='luckee', password='paswd@123')
>>>>>>> 7169453b7522f23b20da633c39bf2cc33adbfa69
    stdin, stdout, stderr = ssh.exec_command('uptime')
    print "Output: \n", stdout.readlines()
except paramiko.SSHException:
    print "Error: \n", stderr.readlines()
finally:
    ssh.close()
    print "Active SSH connection closed"
