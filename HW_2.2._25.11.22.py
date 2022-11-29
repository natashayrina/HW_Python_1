#Задача2.
# Задайте список из n чисел последовательности (1 + 1/n)^n.
# Вывестив консоль сам список и сумму его элементов.

n = int(input("Введите количесвто элементов списка: "))
my_list = []
for i in range (1, n+1):
    my_list.append (round((1+1/n)**n, 2))
print(my_list)
print(round(sum(my_list)))
