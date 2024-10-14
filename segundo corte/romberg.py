import numpy as np
from math import *
def f(x):
    return x**2


def trapecios(a,b,f,n):
    x=np.linspace(a,b,n+1)
    dx=(b-a)
    A=0
    for i in range(1,len(x)-1):
        A+=(2*f(x[i]))
    
    I=dx*(f(x[0])+A+f(x[n]))/(2*n)
    return I

def romberg(a,b,n,f):
    matriz=np.zeros((n,n))
    col_act=0
    for i in range(n):
        if i==0:
            for j in range(n):
                matriz[j][i]=trapecios(a,b,f,2**j)
        else:
            col_act+=1
            for j in range(col_act,n):
                matriz[j][i]=((matriz[j][i-1]*(4**(i)))-matriz[j-1][i-1])/(4**(i)-1)

    print(matriz)

a=0
b=3
n=3
romberg(a,b,n,f)
