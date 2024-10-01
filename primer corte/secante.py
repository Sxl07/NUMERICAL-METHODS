from math import *

def g(x):
  return (x+sqrt(x**2+4*(6.21)**2))/2 - 16

def err(xnew,xold):
  return abs((xnew-xold)/xnew)
  
def derivada(f, x, n=1, h=1e-6):
  if n == 1:
      return (f(x + h) - f(x)) / h
  else:
      f_prime = lambda x: derivada(f, x, n-1, h)
      return (f_prime(x + h) - f_prime(x)) / h
    
def der(x0,x1,f):
  return(f(x0)-f(x1))/((x0-x1))

def sec(x0,x1,tol):
  for i in range(50):
    derivate=der(x0,x1,g)
    pos=x0-g(x0)/derivate
    if err(pos,x0)<tol:
      return pos
    else:
      x0=x1
      x1=pos

a=-1
b=20
tol=10**(-6)
print(sec(a,b,tol))