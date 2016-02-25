#!/usr/bin/python

my_str = raw_input( "Enter a word: ") 

rev_str = reversed(my_str)

if list(my_str) == list(rev_str):
   print "Word is palindrome"
else: 
   print "Word is not palindrome"
