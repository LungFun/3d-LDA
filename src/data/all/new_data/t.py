import sys



def get(n):
    K,L,G = 3,4,5
    Klen = L * G
    Llen = G
    if n >= K * L * G:
        print 'must be less than', K * L * G
    k = n / Klen
    l = (n - k * Klen) / Llen
    g = n - k * Klen - l * Llen
    print k,l,g


if __name__ == '__main__':
    for i in range(60):
        get(int(i))
