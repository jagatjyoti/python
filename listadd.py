#!/usr/bin/python

values = input("Enter some numbers separated by a comma : ")
list = []
total = 0
for i in values:
  list.append(i)
  
for values in list: 
  total = total + values
  
print total
