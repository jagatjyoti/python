#!/usr/bin/python

try:
  fo = open("file.txt", "wb+")
  fo.write( "Python is a great language and its fun to learn \n")
  fo.read()
  fo.close()
except IOError:
  print "Not able to open file, some error"
else: 
  print "Intended operations completed successfully"
