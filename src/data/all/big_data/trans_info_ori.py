import sys

with open(sys.argv[1]) as fp:
    for line in fp:
        line = line.strip()
        if ':' not in line:
            #print line
            pass
        else:
            print ' '.join([i.split(':')[0] for i in line.split()])
