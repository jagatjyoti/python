#!/usr/bin/python

a = 21
b = 10
list = [ 1, 2, 3, 4, 5 ] ;

if ( a in list) :
   print "a is in the list"
else:
   print "a is not in the list"

if ( b in list) :
   print "b is in the list"
else:
   print "b is not in the list"

a = 4

if ( a in list ) : 
   print "a is in the list"
else:
   print "a is not in the list"

print "All tested successfully !!!"
