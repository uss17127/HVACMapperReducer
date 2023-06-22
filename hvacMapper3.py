#!/usr/bin/env python 

from datetime import datetime
import sys
# input comes from STDIN (standard input)
starttime_object = datetime.strptime('09:00:00', '%H:%M:%S')
stoptime_object = datetime.strptime('17:00:00', '%H:%M:%S')
actualtime_object = '00'
for line in sys.stdin:
    # remove leading and trailing whit
    line = line.strip()
    # split the line into data values
    data = line.split(',')
    res = True
    try:
        res = bool(datetime.strptime(data[1], '%H:%M:%S'))
    except ValueError:
        res = False
    # print line                                                                             
    if (res == True):
        actualtime_object = datetime.strptime(data[1],'%H:%M:%S')
        if (actualtime_object.time() >= starttime_object.time() and actualtime_object.time()
< stoptime_object.time()):
            print(str(int(data[6]))+ ',' + actualtime_object.strftime('%H') + ',' + str(int(data[3])))
