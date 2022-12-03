# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# (подробности в конце записи семинара).
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

n = int(input("Введите длину списка: "))
list_1 = []

for i in range(n):
    list_1.append(round(random.uniform(0, 100), 2))
print(list_1)

list_2 = []
x = 0

for i in range (len(list_1)):
    list_2. append(round(list_1[i] - int(list_1[i]), 2))

list_2.sort()

print (max(list_2) - min(list_2))
