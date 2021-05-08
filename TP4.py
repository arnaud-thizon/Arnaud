#TP4, Etude des fonctions par la Dichotomie


import math
from math import cos
from math import exp
from math import tan
from math import log
from math import sin



def Dichotomie(f,a0,b0,epsilon,Nitermax):
    an=a0
    bn=b0
    e=epsilon
    n=0
    while abs(bn-an) > e and n < Nitermax:
        m=(an+bn)/2
        if f(an)*f(m)<=0:
            bn=m
        else:
            an=m
        n+=1
    return m, n

##def f1(x):
##    return (x**4)+(3*x)-9
##
##print(Dichotomie(f1, 1 ,2, 10**(-6), 50000))


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
print(Dichotomie(f1,0,2,1e-10,5e4))
print('f2')
print(Dichotomie(f2,0,1,1e-10,5e4))
print('f3')
print(Dichotomie(f3,1,2,1e-10,5e4))
print('f4')
print(Dichotomie(f4,2,3,1e-10,5e4))
print('f5')
print(Dichotomie(f5,1,2,1e-10,5e4))
print('f6')
print(Dichotomie(f6,1,2,1e-10,5e4))
print('f7')
print(Dichotomie(f7,1,2,1e-10,5e4))
print('f8')
print(Dichotomie(f8,2,3,1e-10,5e4))
print('f9')
print(Dichotomie(f9,2,3,1e-10,5e4))
print('f10')
print(Dichotomie(f10,1,2,1e-10,5e4))
