#Question 2 Fonction sécante:

from math import cos
from math import exp
from math import tan
from math import log
from math import sin


def secante(f,x0,x1,epsilon,Nitermax):
    e = epsilon
    n = 0
    while abs(x1-x0)>e and n<Nitermax:
        x2 = (x0*f(x1)-x1*f(x0))/(f(x1)-f(x0))
        x0 = x1
        x1 = x2
        n+=1
    return x1,abs(x1-x0),n


#Equations

def f1(x):
    return x**4+3*x-9

def f2(x):
    return x-3*cos(x)+2

def f3(x):
    return x*exp(x)-7

def f4(x):
    return exp(x)-x-10

def f5(x):
    return 2*tan(x)-x-5

def f6(x):
    return (x**2)+3-exp(x)

def f7(x):
    return 3*x+4*log(x)-7

def f8(x):
    return (x**4)-2*(x**2)+4*x-17

def f9(x):
    return exp(x)-2*sin(x)-7

def f10(x):
    return log((x**2)+4)*exp(x)-10

#Affichage
print('f1')
print(secante(f1,1,2,1e-10,5e4))
print('f2')
print(secante(f2,-4,-3,1e-10,5e4))
print('f3')
print(secante(f3,1,2,1e-10,5e4))
print('f4')
print(secante(f4,2,3,1e-10,5e4))
print('f5')
print(secante(f5,1,2,1e-10,5e4))
print('f6')
print(secante(f6,1,2,1e-10,5e4))
print('f7')
print(secante(f7,1,2,1e-10,5e4))
print('f8')
print(secante(f8,2,3,1e-10,5e4))
print('f9')
print(secante(f9,2,3,1e-10,5e4))
print('f10')
print(secante(f10,1,2,1e-10,5e4))
