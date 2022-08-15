from sympy import *

x = Symbol('x')

f = (1 / 2) * x ** 2

integ = integrate(f, (x, 0, 2))
print(integ)
