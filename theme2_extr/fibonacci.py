# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 12:09:03 2020

@author: Nikita
"""
import math

'''
Реализовать функцию, осуществляющую поиск экстремума
функции одной переменной методом чисел Фибоначчи. Представить
визуализацию данного метода.
'''

#Исходная функция
def F(x):
    return (x-1)**2+x**4
 
#Число Фибоначчи
def Fib(n):
    return (((1+math.sqrt(5))/2)**n - ((1-math.sqrt(5))/2)**n)/math.sqrt(5)

#main
def methFib(a,b,n):
    x1 = a + (b-a)*Fib(n-2)/Fib(n)
    x2 = a + (b-a)*Fib(n-1)/Fib(n)
    F1 = F(x1)
    F2 = F(x2)
    while n > 1:
        n -= 1
        if F1 > F2:
            a = x1;x1 = x2;x2 = b - (x1 - a)
            F1 = F2;F2 = F(x2)
        else:
            b = x2;x2 = x1;x1 = a + (b - x2)
            F2 = F1;F1 = F(x1)
    return (x1+x2)/2

print(methFib(-5,15,21))
