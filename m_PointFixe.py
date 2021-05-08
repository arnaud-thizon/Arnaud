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
def g00(x):
    return(1+sin(x))/2

#equations

def g1(x):
    return (9-3*x)**(1/4)

def g2(x):
    return math.acos((x+2)/3)

def g2n(x):
    return -math.acos((x+2)/3)

def g3(x):
    return math.log(7/x)

def g4(x):
    return math.log(10+x)

def g4n(x):
    return math.exp(x)-10

def g5(x):
    return math.atan((x+5)/2)

def g6(x):
    return math.log((x**2)+3)

def g7(x):
    return (-4*(math.log(x))+7)/3

def g8(x):
    return (17-4*x+2*(x**2))**(1/4)

def g8n(x):
    return -((17-4*x+2*(x**2))**(1/4))

def g9(x):
    return math.log(7+2*sin(x))

def g10(x):
    return math.log(10/math.log((x**2)+4))

print('g0')
print(PointFixe(g0,0,1e-10,5e4))

print('g00')
print(PointFixe(g00,0,1e-10,5e4))

print('g1')
print(PointFixe(g1,0,1e-10,5e4))

print('g2')
print(PointFixe(g2,0,1e-10,5e4))

print('g2n')
print(PointFixe(g2n,0,1e-10,5e4))

print('g3')
print(PointFixe(g3,1,1e-10,5e4))

print('g4')
print(PointFixe(g4,0,1e-10,5e4))

print('g4n')
print(PointFixe(g4n,0,1e-10,5e4))

print('g5')
print(PointFixe(g5,0,1e-10,5e4))

print('g6')
print(PointFixe(g6,0,1e-10,5e4))

print('g7')
print(PointFixe(g7,1,1e-10,5e4))

print('g8')
print(PointFixe(g8,0,1e-10,5e4))

print('g8n')
print(PointFixe(g8n,0,1e-10,5e4))

print('g9')
print(PointFixe(g9,0,1e-10,5e4))

print('g10')
print(PointFixe(g10,1,1e-10,5e4))
