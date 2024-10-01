import numpy as np
from math import *
def f(x):
    return exp(x**2)

def sumaRiemann(a,b,f,n):
    dx=(b-a)/n
    A=0
    x=np.linspace(a,b,n+1)
    for i in range(0,len(x)-1):
        A+=dx*f((x[i]+x[i+1])/2)
    return A

a=0
b=1
n=10
print(sumaRiemann(a,b,f,n))