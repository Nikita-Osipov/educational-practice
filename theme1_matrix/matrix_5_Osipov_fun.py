# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 14:14:45 2020

@author: Nikita
"""

import numpy as np

'''
Матрицу m x n заполнить
натуральными числами от 1 до m
x n по спирали, начинающейся в
левом верхнем углу в
соответствии с приведенной
схемой.
'''

#main
def spiral(m,n):
    a = np.arange(n*m).reshape(m,n)#Матрица m x n, заполненная числами от 0 до m*n-1
    k = 1
    for i in range(m):
        if i % 2 == 0:
            for j in range(n):
                a[i][j] = k
                k += 1
        else:
            for j in range(n):
                a[i][n-j-1] = k
                k +=1
    return a
    
print(spiral(5,7))