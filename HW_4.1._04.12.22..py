# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (от 0 до 100) многочлена
# и записать в файл многочлен степени k.
# Пример: если k = 2, то многочлены могут быть  2*х **2 + 4*х+5=0

import random

n = int(input("Введите степень "))
x = ''
for k in range(n, -1, -1):
    if k == 1:
        x += f'{random.randint(0, 100)}*x + '
    elif k == 0:
        x += f'{random.randint(0, 100)} '
    else:
        x += f'{random.randint(0,100)}*x**{k} + '


fyle_out = open ("output.txt", "w")
fyle_out.write(x)
fyle_out.close()
print(x)



