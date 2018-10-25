import sys

with open(sys.argv[1]) as fp:
    for line in fp:
        line = line.strip()
        if ':' not in line:
            print line
        else:
            #print ' '.join([i.split(':')[0] for i in line.split()])
            res = []
            for k_v in line.split():
                k,v = k_v.split(':')
                n = (int(v) / 300) + 1 #5min one time
                res += [k] * n
            print ' '.join(res)
