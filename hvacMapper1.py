#!/usr/bin/env python

import sys

#input comes from STDIN (standard input)
for line in sys.stdin:
     # remove leading and trailing whitespace
     line = line.strip()
     # split the line into data values
     data = line.split(',')
     # print line
     if (data[2].isdigit()):
          print(str(int(data[4])) + ',' + str(abs(int(data[2])-int(data[3]))))
