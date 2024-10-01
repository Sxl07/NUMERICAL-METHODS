from math import *

def g(x):
    return 2*sin(sqrt(x))-sqrt(x)

def err(xnew, xold):
    return abs((xnew - xold) / xnew)

def ridder(f, a, b, tol):
    if f(a) * f(b) > 0:
        print("Intervalo mal planteado: f(a) y f(b) deben tener signos opuestos.")
        return None
    else:
        xold = (a + b) / 2
        count = 1
        while True:
            m = (a + b) / 2
            f_a = f(a)
            f_b = f(b)
            f_m = f(m)
            d = (f_m ** 2 - f_a * f_b) ** 0.5
            if d == 0:
                print("División por cero en el cálculo de d.")
                return None
            sign = 1 if f_a > f_b else -1
            xnew = m + sign * (m - a) * f_m / d

            print(f"{count}: {xnew}")

            if err(xnew, xold) < tol:
                return xnew

            f_xnew = f(xnew)

            if f_m * f_xnew < 0:
                a = m
                b = xnew
            elif f_a * f_xnew < 0:
                b = xnew
            else:
                a = xnew

            xold = xnew
            count += 1
            if abs(a - b) < tol:
                return xnew

tol = 1e-6
a = 0
b = 5
raiz = ridder(g, a, b, tol)
print(f"Raíz encontrada: {raiz}")
