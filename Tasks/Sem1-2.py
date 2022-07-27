# 1. По двум заданным числам проверить является ли одно квадратом второго


from math import trunc
from random import randint


def Square(a, b):
    if a*a == b:
        print('a^2 = b')
    elif b*b == a:
        print('b^2 = a')
    else:
        print('НЕ является')


# Square(a=int(input("Введите первое число: ")),
#        b=int(input('Введите второе число: ')))


# 2. Найти максимальное из пяти чисел


def Maxi(x):
    m = 0
    for i in x:
        if i > m:
            m = i
    return (m)


# lst = [randint(-10, 50) for i in range(5)]
# print(f'{lst} ---> {Maxi(lst)}')

# 3. Вывести на экран числа от -N до N

lst = [i for i in range(-5, 6)]
# print (lst)

# 4. Показать первую цифру дробной части числа


def drob(a):
    a = trunc(a % 1 * 10)
    return a


# print(drob(float(input())))



# 5. Дано число. Проверить кратно ли оно 5 и 10 или 15 но не 30

def kratno (num):
    if (num%10 == 0 or num%15 == 0) and num % 30 != 0:
        print('Число подходит')
    else:
        print('Число не подходит')

# kratno (int(input('Введите чило: ')))

# 6. Дано число обозначающее день недели. Вывести его название и указать является ли он выходным.


def dey_week(day):
    if day >= 1 and day <= 7:
        if day >= 1 and day <= 5:
            print('не является выходным днем')
        if day >= 6 and day <= 7:
            print('является выходным днем')
    else:
        print('такого дня не существует')

# dey_week(day=int(input('Введите день недели от 1 до 7: ')))


# 7. Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат


def to_bool(x):
    if x == 0:
        return False
    return True


def Ex2():
    for x in range(2):
        for y in range(2):
            for z in range(2):
                if (not(to_bool(x) or to_bool(y) or to_bool(z)) == (not(to_bool(x)) and not(to_bool(y)) and not(to_bool(z)))) == False:
                    return False
    return True

print(Ex2())

# 8. Сообщить в какой четверти координатной плоскости или на какой оси находится точка с координатами Х и У


def coordinate_plane(x, y):
    if x == 0 and y == 0:
        print('Данная точка является началом координат.')
    elif x != 0 and y == 0:
        print('Данная точка лежит на оси X')
    elif x == 0 and y != 0:
        print('Данная точка лежит на оси Y')
    elif x > 0 and y > 0:
        print('Данная точка лежит в четверти 1')
    elif x < 0 and y > 0:
        print('Данная точка лежит в четверти 2')
    elif x < 0 and y < 0:
        print('Данная точка лежит в четверти 3')
    elif x > 0 and y < 0:
        print('Данная точка лежит в четверти 4')
    else:
        print('Данные введены не верно')


# coordinate_plane(x=int(input('Введите координату X: ')),
#                  y=int(input('Введите координату Y: ')))

# 9. Указав номер четверти прямоугольной системы координат, показать допустимые значения координат для точек этой четверти

def points_quarter(num):
    if num == 1:
        print('В данной четверти координаты могут быть в следующем диапазоне: x > 0, y > 0')
    elif num == 2:
        print('В данной четверти координаты могут быть в следующем диапазоне: x < 0, y > 0')
    elif num == 3:
        print('В данной четверти координаты могут быть в следующем диапазоне: x < 0, y < 0')
    elif num == 4:
        print('В данной четверти координаты могут быть в следующем диапазоне: x > 0, y < 0')
    else:
        print('Данной четверти не существует')

# points_quarter(num = int(input('Введите номер четверти: ')))

# 10. Найти расстояние между двумя точками 2D пространства

# print('Введите координаты точки А:')
# x_A = float(input('x = '))
# y_A = float(input('y = '))
# print('Введите координаты точки B:')
# x_B = float(input('x = '))
# y_B = float(input('y = '))

# # X = (x_A - x_B)**2
# # Y = (y_A - y_B)**2
# # AB = round(((X + Y) ** 0.5),3)

# AB = round((((x_A - x_B)**2 + (y_A - y_B)**2) ** 0.5),3)
# print(AB)
