# Задача4.
# ДОПОЛНИТЕЛЬНО, НО НЕОБЯЗАТЕЛЬНО:
# Написать программу, которая состоит 4 из этапов:
# - создает список из рандомных четырех значных чисел
# - принимает с консоли цифру и удаляет ее из всех элементов списка
# - цифры каждого элемента суммирует пока результат не станет однозначным числом
# - из финального списка убирает все дублирующиеся элементы
# - после каждого этапа выводить результат в консоль
# Пример:
# - 1 этап: [2634, 6934, 7286, 3353, 4602, 3176, 3796]
# - 2 этап: Введите цифру: 3
# - 2 этап: [264, 694, 7286, 5, 4602, 176, 796]
# - 3 этап: 264 -> 2+6+4 -> 12 -> 1+2 -> 3
# - 3 этап: [3, 1, 5, 5, 3, 5, 4]
# - 4 этап: [3, 1, 5, 4]

import random

n = int(input("Введите длину списка: "))
list_1 = []

for i in range(n):
    list_1.append(random.randint(1000, 9999))
print(list_1)


list_2 = list_1
list_2 = list(map(str,list_2))
print (list_2)

num_for_delite = input("Какую цифру удалить?: ")
for i in range(len(list_2)):
    if num_for_delite in list_2[i]:
        element = list_2[i]
        element = element.replace(num_for_delite, "")
        my_str = ""
        for x in element:
            my_str+=x
        list_2 [i] = my_str
list_2 = list(map(int, list_2))
print(list_2)

num = 0
sum = 0

for i in range (len(list_2)):
    while list_2[i] > 0:
        num = list_2[i]%10
        if list_2[i]!=0:
            sum+=num
        num = num/10

print(list_2)

