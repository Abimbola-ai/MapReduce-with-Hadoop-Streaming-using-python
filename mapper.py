"""mapper.py"""


#!/usr/bin/python

import sys

# input comes from STDIN (standard input)


for line in sys.stdin:
    line = line.strip()
    line = line.split(",")
    
    if len(line) >= 2:
        course = line[3]
        name = line[0]
        grade = line[2]
    print('%s\t%s\t%s' % (course, grade, name))
