
import time
import sys

def ts2_w_h(ts):
    one_day_total_seconds = 24 * 60 * 60
    time_local = time.localtime(ts)
    hours   = int(time.strftime("%H", time_local))
    minutes = int(time.strftime("%M", time_local))
    seconds = int(time.strftime("%S", time_local))
    #print hours, minutes, seconds
    totay_total_seconds = hours * 60 * 60 + minutes * 60 + seconds
    #print totay_total_seconds
    weekday = int(time.strftime("%w", time_local))
    #print weekday
    if weekday == 0: weekday = 7
    total_seconds_since_monday = (weekday - 1) * one_day_total_seconds \
                           + totay_total_seconds
    
    return total_seconds_since_monday

#print ts2_w_h(1501942696 )
#print ts2_w_h(1501942696 - 80296 -1)

with open(sys.argv[1]) as fp:
    for line in fp:
        line = line.strip()
        ts_sp = line.split()
        if len(ts_sp) == 1 and int(line) < 100000000:
            print(line)
            #pass
        #elif len(ts_sp) > 50:
        else:
           print(' '.join([ str(ts2_w_h(int(ts))) for ts in ts_sp]))
