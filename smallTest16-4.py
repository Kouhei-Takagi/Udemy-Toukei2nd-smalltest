from sympy import *

x = Symbol('x')

f = (1 / 8) * x ** 2

integ = integrate(f, (x, 0, 4))
print(integ)