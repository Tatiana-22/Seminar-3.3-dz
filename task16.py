'''Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
*Пример:*
5
    1 2 3 4 5
    3
    -> 1'''

import random
list = [random.randint(0,9) for i in range(9)]
print(list)
naturalNum = int (input('Введите натуральное число N: '))
print(naturalNum)
counts=0
for i in range(0,len(list)):
    if (naturalNum == list[i]):
        counts+=1
print(counts)
