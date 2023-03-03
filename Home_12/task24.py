#   Задача 24: 
#   В фермерском хозяйстве в Карелии выращивают чернику. 
#   Она растет на круглой грядке, причем кусты высажены только по окружности. 
#   Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
#   Эти кусты обладают разной урожайностью, поэтому ко времени сбора на 
#   них выросло различное число ягод – на i-ом кусте выросло ai ягод.
#   В этом фермерском хозяйстве внедрена система автоматического сбора 
#   черники. Эта система состоит из управляющего модуля и нескольких 
#   собирающих модулей. Собирающий модуль за один заход, находясь непосредственно
#   перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
#   Напишите программу для нахождения максимального числа ягод, которое может 
#   собрать за один заход собирающий модуль, находясь перед некоторым кустом 
#   заданной во входном файле грядки.
import random
n = int(input())
a = []
sum, sum_max = 0, 0
for i in range(n):
    a.append(random.randint(1,10))
print(a)
a = [a[i]] + a + [a[0]]
print(a)
for i in range(len(a) - 2):
    sum = a[i] + a[i + 1] + a[i + 2]
    if sum > sum_max:
        sum_max = sum
print(sum_max)