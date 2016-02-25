#!/usr/bin/pyton

fo = open( "foo.txt", "rw")
str = fo.read()
print "Reading string: ", str
fo.close()
