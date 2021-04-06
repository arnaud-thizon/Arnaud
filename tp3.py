
'''Ma123'''

from math import sin
from math import cos
from math import tan
from math import exp

from math import log

def Newton(f,fder,x0,epsilon,Nitermax):
    xold = x0
    xnew = xold - f(xold)/fder(xold)
    n = 1
    while abs(xnew-xold)>epsilon and n<Nitermax:
        xold = xnew
        xnew = xold - f(xold)/fder(xold)
        n = n+1
    return xnew,n

#test
def f0(x):
    return 2*x-sin(x)-1
def f0der(x):
    return 2-cos(x)

#Equations

def f1(x):
    return x**4+3*x-9
def f1der(x):
    return 4*x**3+3

def f2(x):
    return x-3*cos(x)+2
def f2der(x):
    return 1+3*sin(x)

def f3(x):
    return x*exp(x)-7
def f3der(x):
    return exp(x)+x*exp(x)

def f4(x):
    return exp(x)-x-10
def f4der(x):
    return exp(x)-1

def f5(x):
    return 2*tan(x)-x-5
def f5der(x):
    return 1+2*(tan(x)**2)

def f6(x):
    return (x**2)+3-exp(x)
def f6der(x):
    return 2*x-exp(x)

def f7(x):
    return 3*x+4*log(x)-7
def f7der(x):
    return 3+4/x

def f8(x):
    return (x**4)-2*(x**2)+4*x-17
def f8der(x):
    return 4*(x**3)-4*x+4

def f9(x):
    return exp(x)-2*sin(x)-7
def f9der(x):
    return exp(x)-2*cos(x)

def f10(x):
    return log((x**2)+4)*exp(x)-10
def f10der(x):
    return exp(x)/((x**2)+4)+log((x**2)+4)*exp(x)

#Affichage
print('f0')
print(Newton(f0,f0der,0,1e-10,5e4))

print('f1')
print(Newton(f1,f1der,0,1e-10,5e4))

print('f2')
print(Newton(f2,f2der,0,1e-10,5e4))

print('f3')
print(Newton(f3,f3der,0,1e-10,5e4))

print('f4')

print(Newton(f4,f4der,1,1e-10,5e4))

print('f5')
print(Newton(f5,f5der,1,1e-10,5e4))

print('f6')
print(Newton(f6,f6der,0,1e-10,5e4))

print('f7')
print(Newton(f7,f7der,1,1e-10,5e4))

print('f8')
print(Newton(f8,f8der,0,1e-10,5e4))

print('f8n')
print(Newton(f8,f8der,-3,1e-10,5e4))

print('f9')
print(Newton(f9,f9der,0,1e-10,5e4))

print('f10')
print(Newton(f10,f10der,0,1e-10,5e4))

