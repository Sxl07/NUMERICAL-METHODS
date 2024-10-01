from math import *

def g(x):
  return exp(-x)-x

def err(xnew,xold):
  return abs((xnew-xold)/xnew)

def bisection(f,a,b,tol):
  if f(a)*f(b)>0:
    print("mal planteado")
    return
  else:
    xold=a
    xnew=b
    count=1
    while err(xnew,xold)>tol:
      xold=xnew
      xnew=(a+b)/2
      print(count,xnew)
      if f(xnew)*f(a)>0:
        a=xnew
      else:
        b=xnew
      count+=1
    return xnew

tol=10**(-6)
a=0
b=5
print(bisection(g,a,b,tol))