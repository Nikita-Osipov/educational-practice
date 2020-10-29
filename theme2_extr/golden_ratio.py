# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 11:58:08 2020

@author: Nikita
"""
import math 

'''
Реализовать функцию, осуществляющую поиск экстремума
функции одной переменной методом золотого сечения. Представить
визуализацию данного метода
'''

#исходная функция
def F(x):
    return (x-1)**2+x**4

#main
def methGoldenR(a,b,l):
    fi = (1+math.sqrt(5))/2
    while abs(b-a) > l:
        x1 = b - (b-a)/fi
        x2 = a + (b-a)/fi
        F1 = F(x1)
        F2 = F(x2)
        if F1 >= F2:
            a = x1
        else:
            b = x2
    return (a+b)/2
        
print(methGoldenR(-5,15,0.001))
  