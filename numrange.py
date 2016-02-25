#!/usr/bin/python

num = int(raw_input("Please enter number: "))

if num in range(0, 100): 
  print "Within range 100"  
elif num in range(101, 1000):
  print "Within range 1000"
elif num in range(1001, 2000):
  print "Within range 2000"
else:
  print "Unknown value!"
