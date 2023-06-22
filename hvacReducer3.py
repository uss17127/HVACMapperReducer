#!/usr/bin/env python
from datetime import datetime
from operator import itemgetter
import sys


#current building
current_blg = None
#current total before finding average
current_total = 0
#count of temp for each building
current_count = 0
#current time
current_time = '00:00:00'
blg = 0
#temp = 0
t = (0,0,0)
final_list =[]


# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # parse the input we got from hvacMapper3.py
    blg, time, temp = line.split(',',2)
    # convert temperature (currently a string) to int
    try:
        time = datetime.strptime(time, '%H')
        temp = int(temp)
        blg = int(blg)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue
    # this IF-switch only works because Hadoop sorts map output
    # by key (here: system) before it is passed to the reducer
    if (current_blg == blg and current_time.time() == time.time()):
        current_total += temp
        current_count += 1
    else:
        if (current_blg and current_time):
 # write result to STDOUT                                                                           
            #print '%s\t%s' % (current_system, average)
            if (current_blg == 2 or current_blg == 12 or current_blg == 19):
                #t = (current_blg, current_time.strftime('%H'), (float(current_total)/float(current_count)))
                avg = (float(current_total)/float(current_count))
                print(str(current_blg) + '\t' + current_time.strftime('%H') + '\t' + str(avg))
                #final_list.append(t)
        current_total = temp
        current_blg = blg
        current_count = 1
        current_time = time
        
#do not forget to output the last word if needed!
if (current_blg == blg and current_time.time() == time.time()):
    #print '%s\t%s' % (current_system, average)
    if (current_blg == 2 or current_blg == 12 or current_blg == 19):
        #t = (current_blg, current_time.strftime('%H'), (float(current_total)/float(current_count)))
        avg = (float(current_total)/float(current_count))
        print(str(current_blg) + '\t' + current_time.strftime('%H') + '\t' + str(avg))
        #final_list.append(t)
