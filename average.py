#!/usr/bin/python

import sys, math

try:
         score1 = int( raw_input( "Enter first score\n"))
         score2 = int( raw_input( "Enter second score\n"))
         score3 = int( raw_input( "Enter third score\n"))
         print "Will try to find out the average" 
         average = (score1 + score2 + score3) / 3
except IOError:
         print "Please enter numeric values only !"
else:
         print "Average of scores is:", average
