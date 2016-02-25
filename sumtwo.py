import sys

if len(sys.argv)==3:
  a=sys.argv[1]
  b=sys.argv[2]
  sum=int(a) + int(b)
  print "The sum is: ", sum
elif len(sys.argv)!=3:
  print "Only two arguments allowed !"
else:
  print "Please enter two numbers as argument with the script. Try again !"
