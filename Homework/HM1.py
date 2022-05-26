# **Задачи домашней работы:**

# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
#     Пример:
#     - 6 -> да
#     - 7 -> да
#     - 1 -> нет

# day = int(input('Введите день недели от 1 до 7: '))
# if day >= 1 and day <= 7:
#     if day >= 1 and day <=5:
#         print('не является выходным днем')
#     if day >= 6 and day <= 7:
#         print('является выходным днем')
# else:
#     print('такого дня не существует')


# 2. Напишите программу, которая принимает на вход координаты точки (X и Y), и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
#     Пример: 
#     - x=34; y=-30 -> 4
#     - x=2; y=4-> 1
#     - x=-34; y=-30 -> 3

# x = int(input('Введите координату X: '))
# y = int(input('Введите координату Y: '))
# if x == 0 and y == 0:
#     print('Данная точка является началом координат.')
# elif x !=0 and y == 0:
#     print('Данная точка лежит на оси X')
# elif x == 0 and y != 0:
#     print('Данная точка лежит на оси Y')
# elif x > 0 and y > 0:
#     print('Данная точка лежит в четверти 1')
# elif x < 0 and y > 0:
#     print('Данная точка лежит в четверти 2')
# elif x < 0 and y < 0:
#     print('Данная точка лежит в четверти 3')
# elif x > 0 and y < 0:
#     print('Данная точка лежит в четверти 4')
# else:
#     print('Данные введены не верно')



# 3. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

# num = int(input('Введите номер четверти: '))
# if num == 1:
#     print('В данной четверти координаты могут быть в следующем диапазоне: x > 0, y > 0')
# elif num == 2:
#     print('В данной четверти координаты могут быть в следующем диапазоне: x < 0, y > 0')
# elif num == 3:
#     print('В данной четверти координаты могут быть в следующем диапазоне: x < 0, y < 0')
# elif num == 4:
#     print('В данной четверти координаты могут быть в следующем диапазоне: x > 0, y < 0')
# else:
#     print('Данной четверти не существует')



# 4. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
#     Пример:
#     - A (3,6); B (2,1) -> 5,09
#     - A (7,-5); B (1,-1) -> 7,21

print('Введите координаты точки А:')
x_A = float(input('x = '))
y_A = float(input('y = '))
print('Введите координаты точки B:')
x_B = float(input('x = '))
y_B = float(input('y = '))

# X = (x_A - x_B)**2
# Y = (y_A - y_B)**2
# AB = round(((X + Y) ** 0.5),3)

AB = round((((x_A - x_B)**2 + (y_A - y_B)**2) ** 0.5),3)
print(AB)

