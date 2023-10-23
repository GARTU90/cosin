#!/usr/bin/env python3
#by gartujuan@gmail.com
#gnu/gpl license
#plotting cosine function
#y = f(x)
#x= [0,2pi]

N=8
A=0
B=200
dx=(B-A)/N
values= range(N+1)
x=A
for jump in values:
    x = jump * dx
    print(x)
    
    