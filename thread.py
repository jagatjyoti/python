#!/usr/bin/python

import pxssh, pexpect, time
from threading import Thread

def remotecopy(name, delay, repeat):

  s = pxssh.pxssh()
  localtime = time.asctime( time.localtime(time.time()) )
  print "Execution of thread started at:", localtime +name

  try:
    var_password = "Root1234"
    remcpy = "rsync -avz ssh --progress /home/techmadmin/Desktop/swp-CSP-Base-6.3.0.0-08-Linux.iso root@192.168.1.102:/home/techmadmin/"

    var_child = pexpect.spawn(remcpy)

    i = var_child.expect(["password:", pexpect.EOF])

    if i==0:
      var_child.sendline(var_password)
      var_child.expect(pexpect.EOF)
    elif i==1:
      print "Connection terminated unexpectedly!"
      pass

  except Exception as e:
      print "Something went wrong."
      print e

      while repeat > 0:
        time.sleep(delay)
        localtime = time.asctime( time.localtime(time.time()) )
        repeat -= 1
      print "Execution of thread ended at:", localtime

def Main():
    t = Thread(target=remotecopy, args=("Timer", 1, 5))
    t.start()
    print "Main completed"

if __name__ == '__main__':
    Main()
