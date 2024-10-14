import numpy as np

# Función a interpolar
def f(x):
    return x**2

# Función para calcular el polinomio de Lagrange en un punto dado
def polinomioLagrange(x, fx, valor):
    n = len(x)
    
    # Inicializar el polinomio de Lagrange en el valor dado
    resultado = 0
    
    # Construir cada término L_i(x) del polinomio de Lagrange
    for i in range(n):
        Li = 1
        for j in range(n):
            if i != j:
                Li *= (valor - x[j]) / (x[i] - x[j])
        
        # Sumar el término f(x_i) * L_i(valor)
        resultado += fx[i] * Li
    
    return resultado

# Parámetros
a = 0
b = 3
n = 4
valor = 4

# Generar los puntos x equidistantes y calcular f(x)
x = np.linspace(a, b, n)
fx = [f(i) for i in x]

# Elegir un valor para evaluar el polinomio de Lagrange
resultado = polinomioLagrange(x, fx, valor)

# Imprimir el resultado
print(f"El valor interpolado en x = {valor} es: {resultado}")
