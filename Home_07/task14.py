<<<<<<< HEAD
#   Задача 14:
#   Требуется вывести все целые степени двойки 
#   (т.е. числа вида 2k), не превосходящие числа N.
#   Пример: 10 → 1 2 4 8

N = int(input())
i = 0
a = ''
if N == 1:
    print(1)
else:
    while 2**i <= N:
        a += str(2**i) + " "
        i+=1
    print(a)
=======
#   Задача 14:
#   Требуется вывести все целые степени двойки 
#   (т.е. числа вида 2k), не превосходящие числа N.
#   Пример: 10 → 1 2 4 8

N = int(input())
i = 0
a = ''
if N == 1:
    print(1)
else:
    while 2**i <= N:
        a += str(2**i) + " "
        i+=1
    print(a)
>>>>>>> b955fee1681419d1fce0f654aee560fe08ac01ac
