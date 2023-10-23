#!/usr/bin/env python3
#by gartujuan@gmail.com
#gnu/gpl license
#plotting cosine function
import math
import matplotlib.pyplot as plt
def f(x):
    Y=math.cos(x)
    return Y
def g(x):
    Y=math.sin(x)
    return Y
#y = f(x)
#x= [0,2pi]

N=10
A=0
B=2*3.1416
dx=(B-A)/N
values= range(N+1)
x=A
X=[]
Y=[]
Z=[]
for jump in values:
    x = A+jump * dx
    X.append(x)

    y=f(x)
    z=g(x)
    Z.append(z)
    Y.append(y)
    #x+=dx
    print(x,y)
plt.plot(X,Y)
plt.scatter(X,Y,color='green')
plt.plot(X,Z)
plt.scatter(X,Z,color='red') 
plt.show()    