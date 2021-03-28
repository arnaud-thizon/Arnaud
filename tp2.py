from math import sin
from math import log
import math

def PointFixe(g,x0,epsilon,Nitermax):
    xold = x0
    xnew = g(xold)
    n = 1
    while abs(xnew-xold)>epsilon and n<Nitermax:
        xold = xnew
        xnew = g(xold)
        n = n+1
    return xnew,n

#test
def g0(x):
    return(1+sin(x))/2
def g1(x):
    return(1+sin(x))/2

print(PointFixe(g0,0,1e-10,5e4))
"""
def g6(x):
    return log((x**2)+3)
print(PointFixe(g6,0,1e-10,5e4))
"""
"""
def g7(x):
    a=math.log(7+2*sin(x))
    return 

print(PointFixe(g7,0,1e-10,5e4))
"""
