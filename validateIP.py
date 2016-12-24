#!/usr/bin/python

address = input("Enter an IP to be validated: ")

def validateIP():
    count = address.count('.')
        if count != 3:
            return False
        else:
            for ele in address:
                if not ele.isdigit():
                    return False
                i = int(ele)
                if i < 0 or i > 255:
                    return False
    return True

result = validateIP()

if result = False:
    print "Entered IP is invalid. Exiting ..."
    sys.exit(1)
else:
    print "IP validation successful !!"
