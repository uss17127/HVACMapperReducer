#!/usr/bin/env python
from operator import itemgetter
import sys

#current building
current_blg = None
#current total before finding average
current_total = 0
#count of temp for each building
current_count = 0
blg = 0
#temp = 0
t = (0,0)
final_list =[]
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # parse the input we got from hvacMapper2.py
    blg, time, temp = line.split(',',2)
    # convert temperature (currently a string) to int
    try:
        temp = int(temp)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue
    # this IF-switch only works because Hadoop sorts map output
    # by key (here: system) before it is passed to the reducer
    if current_blg == blg:
        current_total += temp
        current_count += 1
    else:
        if current_blg:
            # write result to STDOUT
            #print '%s\t%s' % (current_system, average)
            t = (current_blg,(float(current_total)/float(current_count)))
            final_list.append(t)
 	current_total = temp
        current_count = 1
        current_blg = blg
#do not forget to output the last word if needed!
if current_blg == blg:
    #print '%s\t%s' % (current_system, average)
    t = (current_blg, (float(current_total)/float(current_count)))
    final_list.append(t)
    
print(sorted(final_list, key=lambda t: t[1], reverse=True)[:3])
