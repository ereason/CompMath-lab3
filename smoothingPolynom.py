import numpy as np

def calculate(x,Xn,Fxn,order):
    a = np.array([[0.0 for col in range(order + 1)] for row in range(order + 1)])
    b = np.array([0.0 for col in range(order+1)])

    for i in range(len(a)):
        for j in range(len(a[i])):
            for q in range(len(Xn)):
                a[i][j] += pow(Xn[q],i+j)


    for i in range(len(b)):
        for j in range(len(Fxn)):
            b[i]+=Fxn[j]*pow(Xn[j],i)


    buff=np.linalg.solve(a,b)
    arg = [pow(x,col) for col in range(order+1)]
    res = []
    print(a, b,buff)
    for i in range(order+1):
        res.append(arg[i]*buff[i])
    return sum(res)
