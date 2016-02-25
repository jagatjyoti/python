#/usr/bin/python

x = input("Enter first number: ")
y = input("Enter second number: ")
def max_num(x,y):
  if x > y:
    print "Greater number is: ", x
  elif y > x:
    print "Greater number is: ", y
  else: 
    print "Script error!"
