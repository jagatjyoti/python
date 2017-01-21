#!/usr/bin/python

import sys

address = raw_input("Enter an IP to be validated: ")

def validateIP(address):
    count = address.count('.')
    if count != 3:
          return False

    else:
          subnet = address.split('.')
          for each in subnet:
                if not each.isdigit():
                    return False
                i = int(each)
                if i < 0 or i > 255:
                    return False
    return True

result = validateIP(address)

if result == False:
    print "Entered IP is invalid. Exiting ..."
    sys.exit(1)
else:
    print "IP validation successful !!"
