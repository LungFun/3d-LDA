import sys
import os
import math

Dir = sys.argv[1]

f_tassign = os.path.join(Dir, 'model-final.tassign') 
f_phi = os.path.join(Dir, 'model-final.phi')
f_theta = os.path.join(Dir, 'model-final.theta')
def load_phi(f_phi):
    ret = []
    with open(f_phi) as fp:
        for line in fp:
            sp = [float(i) for i in line.strip().split()]
            ret.append(sp)
    return ret

def load_theta(f_theta):
    ret = []
    with open(f_theta) as fp:
        for line in fp:
            sp = [float(i) for i in line.strip().split()]
            ret.append(sp)
    return ret

def perplexity(f_tassign, f_phi, f_theta):
    phi = load_phi(f_phi)
    theta = load_theta(f_theta)
    s = 0.0
    cnt = 0
    with open(f_tassign) as fp:
        doc_num = 0
        for line in fp:
            word2topics = line.strip().split()
            log_w = 0.0
            pro = 1.0
            for w2t in word2topics:
                w, t = w2t.split(':')
                p = 0.0
                for t in range(len(phi)):
                    p += (phi[t][int(w)] * theta[doc_num][t])
                #p = phi[int(t)][int(w)]
                if p > 0:
                    log_w += math.log(p)
                    #pro = p * pro
            if 1:#pro:
            	s += log_w
            cnt += len(word2topics)
            doc_num += 1
    print s, cnt              
    print math.exp(- (s/(cnt * 1.0)))

perplexity(f_tassign, f_phi, f_theta)
