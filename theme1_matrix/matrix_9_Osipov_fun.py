# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 14:27:23 2020

@author: Nikita
"""

import numpy as np
import random

'''
Латинским квадратом порядка n называется квадратная матрица
размером n x n, каждая строка и каждый столбец которой содержат
все числа от 1 до n. Проверить, является ли заданная матрица
латинским квадратом.
'''

#Генерируем случайную матрицу m x n из чисел: 1,...,n 
def randMatrix(n):
    a = np.arange(n**2).reshape(n,n) 
    for i in range(n):
        for j in range(n):
            a[i][j] = random.randint(1,n+1)
    return a

#Сортируем строки и ищем нарушения
def sortF(a1,n):
    for i in range(n-1):
        for j in range(n-i-1):
            if a1[j] == a1[j+1] or a1[j] < 1 or a1[j+1] < 1 or a1[j] > n or a1[j+1] > n:
                return False
            elif a1[j]>a1[j+1]:
                t = a1[j]
                a1[j] = a1[j+1]
                a1[j+1] = t
    return True

#main
def latinS(a):    
    n = len(a)
    print(a)
    transA = np.arange(n**2).reshape(n,n)
    for i in range(n):
        for j in range(n):
            transA[j][i] = a[i][j]
    for i in range(n):
        if sortF(a[i],n) == False:
            return False
        else:
            None
    for i in range(n):
        if sortF(transA[i],n) == False:
            return False    
    return True

print(latinS(randMatrix(4)))
a = [[1,2,3],[2,3,1],[3,1,2]]
print(latinS(a))
a = [[1,2,3,4,5],[4,5,2,3,1],[5,3,4,1,2],[3,1,5,2,4],[2,4,1,5,3]]
print(latinS(a))