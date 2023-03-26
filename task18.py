'''Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
*Пример:*
5
    1 2 3 4 5
    6
    -> 5'''

import random
list = [random.randint(0,5) for i in range(5 )]
print(list)
naturalNum = int (input('Введите натуральное число N: '))
print(naturalNum)
counts=0
min = (naturalNum - list[0])
for i in range(0,len(list)):
    count = (naturalNum - list[i])
    if count < min:
        min = count
        counts = i
print('Самый близкий по величине элемент к заданному числу X: -> ', list[counts])