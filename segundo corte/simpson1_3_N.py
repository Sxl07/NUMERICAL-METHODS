import numpy as np
from math import *
def f(x):
    return sqrt((x**3)+1)


def simpson13n(a,b,f,n):
    x=np.linspace(a,b,n+1)
    print(x)
    dx=(b-a)/n
    print("h",dx)
    I=f(x[0])+f(x[n])
    print("wt",I)
    for i in range(1,len(x)-1):
        print(i)
        if i%2==0:
            I+=2*f(x[i])
        else:
            I+=4*f(x[i])
        print(I)

    return (dx/3)*I

a=1
b=4
n=4
print(simpson13n(a,b,f,n))