#!/usr/bin/python

address = input("Enter an IP to be validated: ")

count = address.count('.')
if count != 3:
    print "Entered IP is invalid. Exiting ..."
else:
    
