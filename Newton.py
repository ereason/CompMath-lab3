import numpy as np

def Newton(x,Xn,Fxn):
    n = len(Xn)
    res = []
    buff = 1.0
    for i in range(n):
        for j in range(n):
            if(j==i):
                continue
            buff *= (x - Xn[j]) / (Xn[i] - Xn[j])
        res.append(buff * Fxn[i])
        buff = 1.0
    return sum(res)