
from math import *

def g(x):
    return 6-16/(2-x)

def punto_fijo(x0, tol, max_iter):
    x = x0
    errores = [x0]

    for _ in range(max_iter):
        x_next = g(x)
        error_relativo = abs((x_next - x) / x_next)

        errores.append(x_next)

        if error_relativo < tol:
            break
        x = x_next

    return x_next, errores

# Parámetros
x0 = 3
tol = 1e-6
max_iter = 1000

# Aplicar el método de punto fijo
valor_aproximado, errores = punto_fijo(x0, tol, max_iter)
print(valor_aproximado)



# Graficar la convergencia
"""plt.plot(errores, marker='o')
plt.xlabel('Número de Iteraciones')
plt.ylabel('Valor de x')
plt.title('Convergencia del Método de Punto Fijo')
plt.axhline(y=3.464102, color='r', linestyle='--', label='√12 exacto')
plt.legend()
plt.grid()
plt.show()
"""