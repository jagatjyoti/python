#!/usr/bin/python


#This script tests whether a password is strong or weak.

import getpass

password = getpass.getpass("Enter password for check: ")
special = '!@#$%^&*()?'
if len(password)>=8 and not password.islower() and not password.isupper() and not password.isalpha() and not password.isdigit() and any ((c in special) for c in password):
  print "Password is strong, well done !"
else: 
  print "Password is weak, please change !"
