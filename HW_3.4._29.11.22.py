# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без применения встроеных методов (арифметически)
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

num = int(input("Введите десятичное число: "))

result = []

while True:
    if num != 0:
        if num % 2 == 0:
            result.append(0)
            a = num // 2
        elif num % 2 == 1:
            result.append(1)
            num= num // 2
    else:
        result.reverse()
        print( *result, sep = '')
        break