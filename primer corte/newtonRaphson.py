from math import *

def g(x):
  return (x-2)

def err(xnew, xold):
  return abs((xnew - xold) / xnew)

def derivada(f, x, n=1, h=1e-6):
  if n == 1:
    return (f(x + h) - f(x)) / h
  else:
    f_prime = lambda x: derivada(f, x, n - 1, h)
    return (f_prime(x + h) - f_prime(x)) / h

def newton(f, x0, tol=1e-6):
  xold = x0
  fx = f(x0)
  fpx = derivada(f, xold)
  if fpx == 0:
    return xold
  xnew = xold - fx / fpx
  count=1
  while err(xnew, xold) > tol:
    xold = xnew
    fx = f(xold)
    fpx = derivada(f, xold)
    print(count,xold)
    if fpx == 0:
      break
    xnew = xold - (fx / fpx)
    count +=1
  return count-1,xold

tol = 10**(-6)
x = 2
print(newton(g, x, tol))
