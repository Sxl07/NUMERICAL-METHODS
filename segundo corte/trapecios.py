import numpy as np
from math import *
def f(x):
    return exp(x**2)


def trapecios(a,b,f,n):
    x=np.linspace(a,b,n+1)
    dx=(b-a)
    A=0
    for i in range(1,len(x)-1):
        A+=(2*f(x[i]))
    
    I=dx*(f(x[0])+A+f(x[n]))/(2*n)
    return I

a=0
b=1
n=10
print(trapecios(a,b,f,n))