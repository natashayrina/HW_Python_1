# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

dict_parts = {'1':'0 <X<=100 and 0<Y<=100', '2':'0<X<=100 and 0>Y>-100', '3':'0>X>-100 and 0>Y>-100', '4':'0>x>-100 and 0<y<100'}

data = int(input("Введите номер четверти системы координат"))
if data == 1:
    print(dict_parts['1'])
elif data == 2:
    print(dict_parts['2'])
elif data == 3:
    print(dict_parts['3'])
else:
    print(dict_parts['4'])

