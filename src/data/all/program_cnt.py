import sys
from collections import defaultdict

program_cnt = defaultdict(int)

pid2name = {}
with open('../../pid2name_tot2.txt') as fp:
    for line in fp:
        id_, name = line.strip().split('\t')
        pid2name[id_] = name

channel2name = {}
with open('../../tvstation2name_tot2.txt') as fp:
    for line in fp:
        id_, name = line.strip().split(',')
        channel2name[id_] = name


#fp_c = open('tv_p_dfile_c.txt.mini')
fp_c = open('tv_p_dfile_c.txt')
channels = fp_c.readlines()

#fp_p = open('tv_p_dfile.txt.mini')
fp_p = open('tv_p_dfile.txt')
programs = fp_p.readlines()

for i in xrange(len(channels)):
    channel_sp =  channels[i].strip().split()
    program_sp =  programs[i].strip().split()  
    if len(channel_sp) > 1:
        for channel, program in zip(channel_sp, program_sp):
                cname = channel2name.get(channel).replace(' ','').replace('\t', '')
                pname = pid2name.get(program).replace(' ','').replace('\t', '')
                #import pdb
                #pdb.set_trace()
                try:
                    program_cnt[cname + '_' + pname] += 1
                except:
                    print i, cname, pname
for p,c in  program_cnt.items():
    print '{}\t{}'.format(p,  c)


