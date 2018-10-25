
import time
import sys

def ts2_w_h(ts):
    time_local = time.localtime(ts)
    w_h = time.strftime("%a_%H", time_local)
    return w_h


with open(sys.argv[1]) as fp:
    for line in fp:
        line = line.strip()
        ts_sp = line.split()
        if len(ts_sp) == 1 and int(line) < 100000000:
            print(line)
        else:
           print(' '.join([ str(ts2_w_h(int(ts))) for ts in ts_sp]))
