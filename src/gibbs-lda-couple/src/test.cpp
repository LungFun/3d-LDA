#include <stdlib.h>
#include<stdio.h>

int main(){

    int K = 5, L =4, G = 5;
    int Klen = L * G;
    int Llen = G;
    int topic = 66;
    int kk = (int)(topic / Klen);
    int ll = (int)((topic - kk * Klen) / Llen);
    int gg = (int)(topic - kk * Klen - ll * Llen);
    printf("%d:(%d,%d,%d)\n", topic, kk,ll,gg);
    return 0;
}
