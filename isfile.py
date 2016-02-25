#!/usr/bin/python

import os.path
file = raw_input( "Enter filename location: ")

if os.path.isfile(file):
    print "File exists at this time"
else: 
    print "No such file"
