#! /usr/bin/python3.5
 
from optparse import OptionParser
import sys
import os
import uuid
import random
 
# Argument validation
 
parser = OptionParser('usage: %prog [path] [depth] [width]')
(opts, args) = parser.parse_args()
 
if len(args) < 3:
        parser.error('please provide path, depth of directory, width of directory')
 
# Function to create binary tree
 
def build_dir_tree(base, depth, width):
    print("Call #%d: Creating directory ..." % depth)
    if depth >= 0:
        curr_depth = depth
        depth -= 1
        for i in range(width):
                os.makedirs('%s/Dir_%d_level_%d' % (base, i, curr_depth))
        dirs = os.walk(base).__next__()[1]
        for dir in dirs:
                newbase = os.path.join(base,dir)
                build_dir_tree(newbase, depth, width)
    else:
        return
 
print('path: %s, depth: %d, width: %d' % (sys.argv[1], int(sys.argv[2]), int(sys.argv[3])))
build_dir_tree(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))
 
print('Binary tree creation successful. Starting to create files recursively ...')
 
# Function to create random files with varied sizes
 
def build_files(base):
    for dirs in os.walk(base):
        d = os.path.join(dirs[0])
        files = random.randint(0, 255)
        i = 0
        while i < files:
            filename = str(uuid.uuid4())
            size = random.randint(1, 1000000)
            with open(os.path.join(d, filename), "w") as f:
                f.write(" " * size)
            i += 1
 
print('path: %s' %(sys.argv[1]))
build_files(sys.argv[1])
 
print('Files generated successfully !!!')
