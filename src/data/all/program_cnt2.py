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


fp_c = open('tv_p_dfile_c.txt.mini')
#fp_c = open('tv_p_dfile_c.txt')
channels = fp_c.readlines()

fp_p = open('tv_p_dfile.txt.mini')
#fp_p = open('tv_p_dfile.txt')
programs = fp_p.readlines()


fp_t = open('tv_p_dfile_t.txt.mini')
#fp_t = open('tv_p_dfile_t.txt')
times = fp_t.readlines()

fp_wc = open('./test/tv_p_dfile_c.txt', 'w+')
fp_wp = open('./test/tv_p_dfile.txt', 'w+') 
fp_wt = open('./test/tv_p_dfile_t.txt', 'w+') 

for i in xrange(len(channels)):
    channel_sp =  channels[i].strip().split()
    program_sp =  programs[i].strip().split()  
    time_sp =  times[i].strip().split()  
    chans = list()
    progs = list()
    tis   = list()
    if len(channel_sp) > 1:
        for channel, program,t  in zip(channel_sp, program_sp, time_sp):
                if channel in ['23', '21', '8']:
                    chans.append(channel)
                    progs.append(program)
                    tis.append(t)
                #cname = channel2name.get(channel).replace(' ','').replace('\t', '')
                #pname = pid2name.get(program).replace(' ','').replace('\t', '')
                #import pdb
                #pdb.set_trace()
                #try:
                #    program_cnt[cname + '_' + pname] += 1
                #except:
                #    print i, cname, pname
    if chans:
    	fp_wc.write(' '.join(chans) + '\n')
    	fp_wp.write(' '.join(progs) + '\n')
        fp_wt.write(' '.join(tis) + '\n')
#for p,c in  program_cnt.items():
#    print '{}\t{}'.format(p,  c)

fp_wc.close()
fp_wp.close()
fp_wt.close()
fp_c.close()
fp_p.close()
fp_t.close()
