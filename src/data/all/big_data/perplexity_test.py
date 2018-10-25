import sys
import os
import math

Dir = sys.argv[1]

f_test = 'data_set/test.txt'
f_word_map = os.path.join(Dir, 'wordmap.txt')
f_phi = os.path.join(Dir, 'model-final.phi')

def load_phi(f_phi):
    ret = []
    with open(f_phi) as fp:
        for line in fp:
            sp = [float(i) for i in line.strip().split()]
            ret.append(sp)
    #ret_d = {}
    #for topic_id in range(len(ret)):
    #    for w_id in range(len(ret[topic_id])):
    #        if not ret_d.has_key(w_id):
    #            ret_d[w_id] = (topic_id, ret[topic_id][w_id])
    #        else:
    #            if ret[topic_id][w_id] > ret_d[w_id][1]:
    #                ret_d[w_id] = (topic_id, ret[topic_id][w_id])
    return ret

def load_word_map(f_word_map):
    ret = {}
    with open(f_word_map) as fp:
        for line in fp:
            sp = line.strip().split()
            if len(sp) == 2:
                ret[int(sp[0])] =  int(sp[1])
    return ret 
            


def perplexity(f_test, f_phi, f_word_map):
    phi = load_phi(f_phi)
    #print phi
    word_map = load_word_map(f_word_map)
    print word_map[10254]
    s = 0.0
    cnt = 0
    with open(f_test) as fp:
        for line in fp:
            if len(line) < 20: continue
            words = line.strip().split()
            log_w = 0.0
            for w in words:
                w_i = word_map.get(int(w))
                if w_i is None:
                    print w
                    continue
                p = 0.0
                for t in range(len(phi)):
                    p +=  phi[t][w_i]
                #if not p:
                #    continue
                if p>0:#p[1] > 0:
                    #log_w += math.log(p[1], 10)
                    log_w += math.log(p)
                else:
                    print(p)
            s += log_w
            cnt += len(words)
    print s, cnt           
    print math.exp( - (s/(cnt * 1.0)))

perplexity(f_test, f_phi, f_word_map)
