import numpy as np

def GetDivDiff(Xn,Fxn, order):
    summ = 0
    for i in range(order):
        buff = 1.0
        for j in range(order):
            if i == j:
                continue
            buff*=(Xn[i] - Xn[j])
        summ += Fxn[i]/buff

    return summ

def Newton(x,Xn,Fxn):
    sum = 0.0
    for i in range(len(Xn)):
        buff = 1.0
        for j in range(i):
            buff*=(x-Xn[j])
        sum+=buff*GetDivDiff(Xn,Fxn,i+1)

    return sum