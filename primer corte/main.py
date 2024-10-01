from math import *

xold = 1
tol=10**(-6)
def g(x):
  return exp(-x)

def err(xnew,xold):
  return abs(xnew-xold)

xnew = g(xold)
error=err(xnew,xold)
while not (error < tol):
  xnew = g(xold)
  error=err(xnew,xold)
  print(error)
  if error < tol:
    print("-----",xnew,"-----")
    break
  xold=xnew

  