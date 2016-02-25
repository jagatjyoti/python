#!/usr/bin/python

import os, sys

def Cat(filename):
  f = open(filename)
  text = f.read()
  print "------", filename
  print text

def main():
  args = sys.argv[1:]
  for arg in args:
     Cat(arg) 

if __name__ == '__main__':
  main()
