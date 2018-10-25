#coding: utf8

last_name = ''
with open('gid2name.txt') as fp:
    for line in fp:
        line = line.strip()
        sp  = line.split(',')
        if not last_name:
            last_name = sp[1]
            print line
        else:
            if sp[1] == '市辖区':
                print sp[0] + ',' + last_name + '辖区'
            else:
                print line
            last_name = sp[1]
            
