#   Задача 32: 
#   Определить индексы элементов массива (списка), 
#   значения которых принадлежат заданному диапазону 
#   (т.е. не меньше заданного минимума и не больше заданного максимума)

import random
n = int(input())
list_elem = [random.randint(1,20) for i in range(n)]
print(list_elem)
min_elem, max_elem = map(int, input().split())
array = []
for i in range(len(list_elem)):
    if min_elem <= list_elem[i] <= max_elem:
        array.append(i)
print(array)
