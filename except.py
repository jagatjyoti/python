#!/usr/bin/python

try:
   fw = open( "abc.txt", "w" )
   fw.write( "This is just a sample writing to the file" );
except IOError:
   print "Error: can't find file for writing or permission issues"
else:
   print "Contents written successfully !"
