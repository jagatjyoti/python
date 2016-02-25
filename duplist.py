#!/usr/bin/python

digits = [ 1, 2, 1, 4, 5, 3, 4, 2, 3, 7, 8 ]
copy = []
for x in digits:
    if digits.count(x) == 1:
        copy.append(x)
            
for y in copy:
    digits.remove(y)
print digits
