# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# 6 -> да
# 7 -> да
# 1 -> нет

data=int(input("Введите цифру - день недели 1 до 7 " ))
if 0 < data < 6:
    print("Это будний день")
else:
    print("Это выходной день")