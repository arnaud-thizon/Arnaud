'tp1 - génie maths'
from math import sin
from math import cos
from math import fabs
z = 1e-8

#question 1
x=0
for n in range(41):
    x=(1+sin(x))/2
    print("g(",n,") =",x)
if 2*x - sin(x)-1 < z :
    print("x(",n,") est une approximation de la solution de 2x=1+sin x")

print("="*70)

#question 3
a=0
for n in range(41):
    a = (1+sin(a))/2
    e = fabs(a-x)
    m = (1/2)**n
    print("g(",n,") =",a)
    print("e(",n,") =",e)
    print("m(",n,") =",m)
    if e <= m :
        print("la majoration est vérifiée")

print("="*70)

#question 4
p=0
n=0
while fabs(p-x) > 1e-5:
    p=(1+sin(p))/2
    n=n+1
print(n)

b=0
n=0
while fabs(b-x) > 1e-10:
    b=(1+sin(b))/2
    n=n+1
print(n)

print("="*70)

#question 5

f=0
e=0
w=0

for n in range(1,41):
    f = (1+sin(f))/2
    e = fabs(f-x)
    v = (e+1)/e
    w = v-(cos(x)/2)
    print("pour n=",n)
    print(v)
    print(w)
