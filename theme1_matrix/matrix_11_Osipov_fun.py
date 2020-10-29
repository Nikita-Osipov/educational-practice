# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 15:09:27 2020

@author: Nikita
"""

import numpy as np
import random

def randMatrix(m,n):
    a = np.arange(m*n).reshape(m,n) 
    for i in range(m):
        for j in range(n):
            a[i][j] = random.randint(0,1)
    return a

def transA(a,m,n):
    trA = np.arange(m*n).reshape(n,m) 
    for i in range(n):
        for j in range(m):
            trA[i][j] = a[j][i]
    return trA

def hlp(a,m,n):
    lst1 = []
    lst2 = []
    step = []
    for i in range(m):
        lst1.append([m-1-i,0])
    for i in range(n-1):
        lst1.append([0,i+1])
    t = 0
    while t < len(lst1):
        s = 1
        step.append(a[lst1[t][0]][lst1[t][1]])
        while True:
            try:
                step.append(a[lst1[t][0]+s][lst1[t][1]+s]) 
                s += 1
            except Exception:
                t += 1  
                lst2.append(step)
                step = []
                break                             
    return lst2
 
def rev(a,m,n):
    a2 = np.arange(m*n).reshape(m,n) 
    for i in range(m):
        for j in range(n):
            a2[i][j] = a[i][n-1-j]
    return a2
           
def fun11(a):
    maxD = 0
    k = 0
    m = len(a)
    n = len(a[0])
    for i in range(m):
        for j in range(n):
            if a[i][j] == 0:
                k += 1
            else:
                if k > maxD:
                    maxD = k
                k = 0
        if k > maxD:
            maxD = k
            k = 0
        k = 0
    k = 0
    trA = transA(a,m,n)
    for i in range(n):
        k = 0
        for j in range(m):
            if trA[i][j] == 0:
                k += 1
            else:
                if k > maxD:
                    maxD = k
                k = 0
        if k > maxD:
            maxD = k
            k = 0
        k = 0
    k = 0
    diag1 = hlp(a,m,n)
    a2 = rev(a,m,n)
    diag2 = hlp(a2,m,n)
    for i in range(m+n-1):
        for j in range(len(diag1[i])):
            if diag1[i][j] == 0:
                k += 1
            else:
                if k >= maxD:
                    maxD = k
                k = 0
        if k > maxD:
            maxD = k
            k = 0
        k = 0
    k = 0
    for i in range(m+n-1):
        for j in range(len(diag2[i])):
            if diag2[i][j] == 0:
                k += 1
            else:
                if k >= maxD:
                    maxD = k
                k = 0
        if k > maxD:
            maxD = k
            k = 0
        k = 0
    k = 0
    return a,maxD  
   
res = fun11(randMatrix(5,5))

print(res[0],res[1])

    
    
    
    
    
    
    
    
    