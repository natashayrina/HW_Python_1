# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16]
# [2, 3, 5, 6] => [12, 15]

import random

n = int(input("Введите длину списка : "))

arr_1 =[]

for i in range (n):
    arr_1.append(random.randint(1, 10))
print(arr_1)


arr_new = []

for i in range (len (arr_1)):
    if i<len(arr_1) / 2:
        arr_new.append(arr_1[i] * arr_1[-1-i])

print(arr_new)