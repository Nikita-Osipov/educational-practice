# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 13:47:14 2020

@author: Nikita
"""

import numpy as np

'''
В таблице из n строк и n столбцов некоторые клетки заняты
шариками, другие свободны. Выбран шарик, который нужно
переместить, и место, куда его нужно переместить. Выбранный
шарик за один шаг перемещается в соседнюю по горизонтали или
вертикали свободную клетку. Требуется выяснить, возможно ли
переместить шарик из начальной клетки в заданную, и если
возможно, то найти путь из наименьшего количества шагов.
'''

#main
def wave(matrixSize,barrier,start,end):
    if start == end:
        return []
    elif end[0] >= matrixSize or end[1] >= matrixSize or end[0] < 0 \
        or end[1] < 0 or start[0] >= matrixSize or \
            start[1] >= matrixSize or start[0] < 0 or start[1] < 0:
        return False
    a = np.arange(matrixSize**2).reshape(matrixSize,matrixSize)
    for i in range(8):
        for j in range(8):
            a[i][j] = 0;
            
    #Зададим значение стенам        
    for i in range(len(barrier)):
        a[barrier[i][0]][barrier[i][1]] = -1
    
    if a[end[0]][end[1]] == -1:
        return False
    elif a[start[0]][start[1]] == -1:
        return False
    
    lst = [start]
    lstNew = []
    size = matrixSize
    a[start[0]][start[1]] = 1
    
    #'Волна'
    while len(lst) != 0:
        for i in range(len(lst)):
            u = [lst[i][0]-1,lst[i][1]]
            d = [lst[i][0]+1,lst[i][1]]
            r = [lst[i][0],lst[i][1]+1]
            l = [lst[i][0],lst[i][1]-1]
            if u[0] >=0 and u[1] >= 0 and u[0] < size and u[1] < size:
                if a[u[0]][u[1]] == 0:
                    a[u[0]][u[1]] = (a[lst[i][0]][lst[i][1]])+1
                    lstNew.append(u)
            if d[0] >=0 and d[1] >= 0 and d[0] < size and d[1] < size:
                if a[d[0]][d[1]] == 0:      
                    a[d[0]][d[1]] = (a[lst[i][0]][lst[i][1]])+1
                    lstNew.append(d)
            if r[0] >=0 and r[1] >= 0 and r[0] < size and r[1] < size:
                if a[r[0]][r[1]] == 0:      
                    a[r[0]][r[1]] = (a[lst[i][0]][lst[i][1]])+1
                    lstNew.append(r)
            if l[0] >=0 and l[1] >= 0 and l[0] < size and l[1] < size:
                if a[l[0]][l[1]] == 0:      
                    a[l[0]][l[1]] = (a[lst[i][0]][lst[i][1]])+1
                    lstNew.append(l)       
        lst = lstNew
        lstNew = []
      
    lstLast = [end]
    dist = a[end[0]][end[1]]
    pos = end
    k = 1
    
    #Восстановление пути
    if dist > 0:
        for i in range(dist):
            if a[pos[0]-1][pos[1]] == dist - k and pos[0]-1 >=0 \
                and pos[1] >=0 and pos[0]-1 < size and pos[1] < size:
                lstLast.append([pos[0]-1,pos[1]])
                pos = [pos[0]-1,pos[1]]
                k +=1
            elif a[pos[0]+1][pos[1]] == dist - k and pos[0]+1 >=0 \
                and pos[1] >=0 and pos[0]+1 < size and pos[1] < size:
                lstLast.append([pos[0]+1,pos[1]])
                pos = [pos[0]+1,pos[1]]
                k +=1
            elif a[pos[0]][pos[1]+1] == dist - k and pos[0] >=0 \
            and pos[1] +1 >=0 and pos[0] < size and pos[1]+1 < size:
                lstLast.append([pos[0],pos[1]+1])
                pos = [pos[0],pos[1]+1]
                k +=1
            elif a[pos[0]][pos[1]-1] == dist - k and pos[0] >=0 \
                and pos[1] -1 >=0 and pos[0] < size and pos[1] -1 < size:
                lstLast.append([pos[0],pos[1]-1])
                pos = [pos[0],pos[1]-1]
                k +=1
    lstLast.reverse()
    return a, lstLast

barrier = [[3,1],[3,2],[3,3],[1,5],[1,6],[4,6]]
start = [1,1]
end = [3,6]
matrixSize = 8
res = wave(matrixSize,barrier,start,end)
print(res[0])
print(res[1])