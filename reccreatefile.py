#!/usr/bin/python
 
import os
import uuid
import random
 
for dirs in os.walk("/home/zarvis"):
    d = os.path.join(dirs[0])
    filename = str(uuid.uuid4())
    size = random.randint(1, 1000000)
    with open(os.path.join(d, filename), "w") as f:
        f.write(" " * size)
