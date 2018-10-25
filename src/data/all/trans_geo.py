import sys


old_id2tv = {}
line_cnt = 0
with open('tv_ids_all_old.txt') as fp:
    for line in fp:
        old_id2tv[line_cnt] = line.strip()
        line_cnt += 1

line_cnt = 0
new_tv2id = {}
with open('tv_ids_all.txt') as fp:
    for line in fp:
        new_tv2id[line.strip()] = line_cnt
        line_cnt += 1


line_cnt = 0
new_id2val = {}
with open(sys.argv[1]) as fp:
    for line in fp:
        line = line.strip()
        if ':' in line:
            new_id2val[line_cnt] = line
            line_cnt += 1

print line_cnt
       
for cnt in range(line_cnt):
    old_tv = old_id2tv[cnt]
    new_id = new_tv2id[old_tv]
     
    val =  new_id2val[new_id]
    vals = []
    for i in val.split():
        v, cnt = i.split(':')
        vals.extend([v] * int(cnt))
    print ' '.join(vals)



