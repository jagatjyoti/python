#!/usr/bin/python

import re

str = "sdfklj...werwlnl\;asjlj192.168.22.1wioruwnlnv"
found = re.search(r'(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})',str)
print found.group()
