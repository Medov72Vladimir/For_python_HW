#   Задача 16: 
#   Требуется вычислить, сколько раз встречается некоторое число
#   X в массиве A[1..N]. Пользователь в первой строке вводит натуральное 
#   число N – количество элементов в массиве. В последующих  строках 
#   записаны N целых чисел Ai. Последняя строка содержит число X
#   *Пример:*
#   5
#   1 2 3 4 5
#   3
#   -> 1

import random
N = int(input("Введи число элементов массива А \n"))
A = [random.randint(1,9) for i in range(N)]
X = int(input("Введи проверочное число X \n"))
count = 0
for i in A:
    if i == X:
        count+=1
print("-------------")
print(*A)
print(f"Число X={X} встречается {count} раз(а)")
