from math import *

def g(x):
  return 20*exp(0.15*x)-100

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

  while err(xnew, xold) > tol and fx<=100:
    print(xold,err(xnew,xold))
    xold = xnew
    fx = f(xold)
    fpx = derivada(f, xold)
    if fpx == 0:
      break
    xnew = xold - fx / fpx
  return xold

tol = 10**(-7)
x = 6
print("----",newton(g, x, tol),"----")
