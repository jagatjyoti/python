#!/usr/bin/python

from os.path import join
import os

filename = raw_input("Enter file to be searched: ")
for root, dirs, files in os.walk('/'):
    print "Searching", root
    if filename in files:
        print "Found file: %s" % join(root, filename)
        break
