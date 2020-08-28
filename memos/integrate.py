from sympy import *
x=Symbol('x')

print(integrate(x**3, (x, -1, 1)))
integrate(sin(x), (x, 0, pi/2))

print(integrate(3 * x ** 2, (x, 0, 2 / 3)) + integrate(6 * x * (1 - x), (x, 2 / 3, 1)))
