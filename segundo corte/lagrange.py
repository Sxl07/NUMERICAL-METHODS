import numpy as np

def f(x):
    return x**2

def polinomioLagrange(x, fx, valor):
    n = len(x)
    
    resultado = 0
    
    for i in range(n):
        Li = 1
        for j in range(n):
            if i != j:
                Li *= (valor - x[j]) / (x[i] - x[j])
        
        resultado += fx[i] * Li
    
    return resultado

a = 0
b = 3
n = 4
valor = 4

x = np.linspace(a, b, n)
fx = [f(i) for i in x]

resultado = polinomioLagrange(x, fx, valor)

print(f"El valor interpolado en x = {valor} es: {resultado}")
