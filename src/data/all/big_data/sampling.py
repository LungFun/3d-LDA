import sys
import random

split = 0.7

training = open('training.txt', 'w+')
test     = open('test.txt', 'w+')

if not training or not test:
    print 'open file failed!'
    sys.exit(1)

with open(sys.argv[1]) as fp:
    for line in fp:
        if len(line) < 20:
            continue
        r =  random.random()
        if r >= split:
           training.write(line)
        else:
           test.write(line)

