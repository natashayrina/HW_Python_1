# Напишите программу, которая принимает на вход координаты двух точек и
# находит расстояние между ними в 2D пространстве
# (НЕОБЯЗАТЕЛЬНО, ПО ЖЕЛАНИЮ: найти растояние в 3D пространстве)
# Пример:
# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21

import math
from math import sqrt

data_XA = int(input("Введите координату первой точки XA: "))
data_YA = int(input("Введите координату первой точки YA: "))
data_XB = int(input("Введите координату второй точки XB: "))
data_YB = int(input("Введите координату второй точки YB: "))

distance_between_points = round(math.sqrt((data_XB - data_XA) ** 2 + (data_YB - data_YA) ** 2), 2)
print(distance_between_points)