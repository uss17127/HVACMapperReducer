#!/usr/bin/env python                                                                         

from operator import itemgetter
import sys

current_system = 0
current_difference = 0
system = 0
t = (0,0)
final_list =[]

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # parse the input we got from hvacMapper1.py
    system, difference = line.split(',',1)
    # convert difference (currently a string) to int
    try:
        difference = int(difference)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue
    # this IF-switch only works because Hadoop sorts map output
    # by key (here: system) before it is passed to the reducer
    if current_system == system:
        current_difference += difference
    else:
        if current_system:
            # write result to STDOUT
            #print '%s\t%s' % (current_system, current_difference)
            t = (current_system, current_difference)
            final_list.append(t)
        current_difference = difference
        current_system = system
#do not forget to output the last word if needed!
if current_system == system:
    #print '%s\t%s' % (current_system, current_difference)
    t = (current_system, current_difference)
    final_list.append(t)

print(sorted(final_list, key=lambda t: t[1], reverse=True)[:3])
