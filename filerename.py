#!/usr/bin/python

import os
from path import path

p = path('/home/emc/python/info')
for files in p:
  os.rename("file.py", "file.sh")
  print "Renamed file:  ", file
