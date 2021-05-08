# -*- coding: utf-8 -*-
"""
Created on Thu May  6 22:56:36 2021

@author: Clément FONTENEAU
"""

import math
import matplotlib.pyplot as mp



def PointFixe(g,x0,epsilon,Nitermax):
    x = x0
    n = 0
    e = epsilon
    ln = []
    lxn = []
    le = []
    while n != Nitermax and abs(g(x)-x)>= e:
        n = n + 1
        x = g(x)
        ln.append(n)
        lxn.append(x)
        le.append(abs(g(x)-x))
        print(g(x))
        print("Itération", n)
        print("écart", abs(g(x)-x))
    return ln, lxn, le

# def f(x):
#     return (9-3*x)**0.25
# res=PointFixe(f, 0, 10**(-15), 100)
# print(res)



def Newton(f,fder,x0,epsilon,Nitermax):
    xold = x0
    # xnew = xold - f(xold)/fder(xold)
    n = 0
    ln = []
    lxn = []
    le = []
    while abs(xold-(xold - f(xold)/fder(xold)))>epsilon and n!=Nitermax:
        n = n+1
        xnew = xold - f(xold)/fder(xold)
        xold = xnew
        ln.append(n)
        lxn.append(xold)
        le.append(abs(xold - xnew))
    return ln, lxn, le


def Dichotomie(f,a0,b0,epsilon,Nitermax):
    an=a0
    bn=b0
    e=epsilon
    n=0
    ln = []
    lan = []
    le = []
    while abs(bn-an) > e and n < Nitermax:
        m=(an+bn)/2
        if f(an)*f(m)<=0:
            bn=m
        else:
            an=m
        n+=1        
        ln.append(n)
        lan.append(an)
        le.append(abs(bn - an))
    return ln, lan, le



def secante(f,x0,x1,epsilon,Nitermax):
    e = epsilon
    n = 0
    ln = []
    lxn = []
    le = []
    while abs(x1-x0)>e and n<Nitermax:
        x2 = (x0*f(x1)-x1*f(x0))/(f(x1)-f(x0))
        x0 = x1
        x1 = x2
        n+=1
        ln.append(n)
        lxn.append(x1)
        le.append(abs(x1 - x0))
    return ln, lxn, le



def fpf(x): #Fonction PointFixe
    return math.log((7/x))

def fdh(x): #Fonction Dichotomie
    return x*math.exp(x)-7

def fn(x): #Fonction Newton
    return x*math.exp(x)-7

def fnder(x): #Fonction Dérivée de Newton
    return math.exp(x)+x*math.exp(x)

def fs(x): # Fonction Sécante
    return x*math.exp(x)-7



Secante = secante(fs,0, 1,10**(-15),100)
Dichotomie = Dichotomie(fdh, 0, 1, 10**(-15), 100)
PointFixe = PointFixe(fpf, 1, 10**(-15),100)
Newton = Newton(fn, fnder, 1, 10**(-15), 100)


    
lx = Dichotomie[0]
ly = [abs(i - Dichotomie[1][-1]) for i in Dichotomie[1]]
mp.plot(lx, ly, 'b', label='Dichotomie')
    
lx = Newton[0]
ly = [abs(i - Newton[1][-1]) for i in Newton[1]]
mp.plot(lx, ly, 'g', label='Newton')
    
lx = Secante[0]
ly = [abs(i - Secante[1][-1]) for i in Secante[1]]
mp.plot(lx, ly, 'r', label='Secante')
    
lx = PointFixe[0]
ly = [abs(i - PointFixe[1][-1]) for i in PointFixe[1]]
mp.plot(lx, ly, 'y', label='PointFixe')
    
mp.semilogy()
mp.legend()
mp.grid()
mp.show()

