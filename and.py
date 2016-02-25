#!/usr/bin/python

import os

a = os.mkdir( "/home/emc/python/test" )
b = os.getcwd()

if ( a and b ):
   print b
   print "All operations succeded !"
else:
   print "Failed miserably !"
   os.rmdir( "/home/emc/python/test" )
