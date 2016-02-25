#!/usr/bin/pyton

import subprocess
cmd = "cat foo.txt | grep -i python"
p = subprocess.Popen(cmd, shell=True, stderr=subprocess.PIPE)
output, err = p.communicate()
print output
print err
