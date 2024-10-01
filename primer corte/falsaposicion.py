from math import *

def g(x):
  return (x**2)-12

def err(xnew,xold):
  return abs((xnew-xold))

def falsaposicion(f,a,b,tol):
    fa=g(a)
    fb=g(b)
    xold=a
    xnew=b
    count=1
    while err(xnew,xold)>tol:
      xold=xnew
      xnew=a-((a-b)*fa)/(fa-fb)
      print(count,xnew,err(xnew,xold))
      if f(xnew)*f(a)>0:
        a=xnew
      else:
        b=xnew
      count+=1
    return xnew

tol=10**(-4)
a=3
b=10
print("----------",falsaposicion(g,a,b,tol),"----------")