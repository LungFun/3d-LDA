import sys

pid2name_file = sys.argv[1]

pid2name = {}
with open(pid2name_file) as fp:
    for line in fp:
        id_, name = line.strip().split('\t')
        pid2name[int(id_)] =  name

with open(sys.argv[2]) as fp:
    for line in fp:
        line = line.strip()
        if 'Topic' in line:
            print line
        else:
            sp = line.split('\t')
            sp = sp[0].split(' ')
            print pid2name[int(sp[0])], sp[-1]

