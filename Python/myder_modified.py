# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 16:50:22 2018

@author: Tom K
@modified by : Asem Hassan on Sep 13 2018
"""

def forwardiff(f,a,b,N):
    h = (b-a)/N
    g=[]
    for k in range(1,N):
        slop = (f(a+k*h)-f(a+(k-1)*h))/h
        g.append(slop)
    return g
    
def backwardiff(f,a,b,N):
    h = (b-a)/N
    g=[]
    for k in range(0,N):
        slop = (f(a+k*h)-f(a+(k-1)*h))/h
        g.append(slop)
    return g

def centraldiff(f,a,b,N):
    h = (b-a)/N
    g=[]
    for k in range(0,N):
        slop = (f(a+(k+1/2)*h)-f(a+(k-1/2)*h))/h
        g.append(slop)
    return g

def centraldiff_2ndord(f,a,b,N):
    h = (b-a)/N
    g=[]
    for k in range(0,N):
        scnd_ord=((1/2)*f(a+(k+1)*h)+(-1/2)*f(a+(k-1)*h))/h
        g.append(scnd_ord)
    return g 

def centraldiff_3rdord(f,a,b,N):
    h = (b-a)/N
    g=[]
    for k in range(0,N):
        thrd_ord=((-1/24)*f(a+(k+3/2)*h)+(27/24)*f(a+(k+1/2)*h)-(27/24)*f(a+(k-1/2)*h)+(1/24)*f(a+(k+3/2)*h))/h
        g.append(thrd_ord)
    return g

def centraldiff_4thord(f,a,b,N):
    h=(b-a)/N
    g=[]
    for k in range(0,N):
        frth_ord=((-1/12)*f(a+(k+2)*h)+(2/3)*f(a+(k+1)*h)-(2/3)*f(a+(k-1)*h)+(1/12)*f(a+(k-2)*h))/h
        g.append(frth_ord)
    return g
                  
def centraldiff_5thord(f,a,b,N):
    h=(b-a)/N
    g=[]
    for k in range(0,N):
        ffth_ord=((3/640)*f(a+(k+5/2)*h)-(25/384)*f(a+(k+3/2)*h)+(75/64)*f(a+(k+1/2)*h)-(75/64)*f(a+(k-1/2)*h)+(25/384)*f(a+(k-3/2)*h)-(3/640)*f(a+(k+5/2)*h))/h
        g.append(ffth_ord)
    return g

def central_second_der(f,a,b,N):
    h=(b-a)/N
    g=[]
    for k in range(0,N):
        scnd_der=(f(a+(k+1)*h)-2*f(a+k*h)+f(a+(k-1)*h))/(h**2)
        g.append(scnd_der)
    return g

def backward_second_der(f,a,b,N):
    h=(b-a)/N
    g=[]
    for k in range(0,N):
        scnd_der=(f(a+k*h)-2*f(a+(k-1)*h)+f(a+(k-2)*h))/(h**2)
        g.append(scnd_der)
    return g

                  

