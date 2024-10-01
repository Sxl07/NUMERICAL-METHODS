import math

def derivada(f, x, n=1, h=1e-4):
  if n == 0:
    return f(x)
  elif n == 1:
    return (f(x + h) - f(x)) / h
  else:
    f_prime = lambda x: derivada(f, x, n - 1, h)
    return (f_prime(x + h) - f_prime(x)) / h

def f(x):
  return math.sqrt(x + 1)

x = -1/13
n = 4
h = 1e-3
valorreal = math.sqrt(12)

count = f(0)
for i in range(1, n):
  p_n = ((x**(i)) * derivada(f, 0, i, h)) / math.factorial(i)
  count += p_n

print(f"El valor real es: {valorreal}")
print(f"La aproximacion de la derivada es: {(math.sqrt(13))*count}")
