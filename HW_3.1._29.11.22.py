# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
import random


import random

n = int(input("Введите длину списка: "))
list_1 = []
list_2 = []
for i in range(n):
    list_1.append(random.randint(1, 100))
print(list_1)

for i in range (len(list_1)):
    list_2 = list_1[1:len(list_1):2]
print(sum(list_2))