from sympy import *

x = Symbol('x')

u = (1 / 2) * x ** 2
integU = integrate(u, (x, 0, 2))
print(integU)

e = (1 / 2) * x ** 3
integX = integrate(e, (x, 0, 2))

print(integX)

print(integX - integU ** 2)
