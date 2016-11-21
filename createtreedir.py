#!/usr/bin/python

import sys
import os

def build_dir_tree(base, depth, width):
    print("Call #%d" % depth)
    if depth >= 0:
        curr_depth = depth
        depth -= 1
        for i in xrange(width):
                # first creating all folder at current depth
                os.makedirs('%s/Dir_%d_level_%d' % (base, i, curr_depth))
        dirs = os.walk(base).next()[1]
        for dir in dirs:
                newbase = os.path.join(base,dir)
                build_dir_tree(newbase, depth, width)
    else:
        return

if not sys.argv[1:]:
        print('No base path given')
        sys.exit(1)

print('path: %s, depth: %d, width: %d' % (sys.argv[1], int(sys.argv[2]), int(sys.argv[3])))
build_dir_tree(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))
