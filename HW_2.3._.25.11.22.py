# Задача3.
# Реализуйте алгоритм перемешивания списка.
# Встроенный алгоритм SHUFFLE не использовать! Реализовать свой метод,



import random

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Исходный список: ", arr)

for i in range(len(arr)):
    j = random.randint(0, len(arr) - 1)
    num = arr.pop(j)
    arr.append(num)
print("Перемешанный список: ", arr)