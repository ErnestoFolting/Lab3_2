
#Із заданою точністю ε обчислити значення функції cos x
import math
eps, x = float(input('eps = ')), float(input('x = '))
Cos = 0
x1 = 1
xn = ((-1) * pow(x,2))/2
n = 1
Cos = Cos + x1 + xn

while abs(xn-x1) >= eps:
    n += 1
    x1 = xn
    xn = pow((-1), n) * pow(x, 2 * n) / (math.factorial(2*n))
    Cos += xn
print(Cos)