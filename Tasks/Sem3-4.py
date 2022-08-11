# 12. Сформировать список из  N членов последовательности.
#     Для N = 5: 1, -3, 9, -27, 81 и т.д.

# N = int(input('Введите число N: '))

# for i in range(N):
#     result = (-3)**i
#     print(result, end = ' ')

# N = 5
# for i in range(N):
#     result = (-3)**i
#     print(result, end = ' ')

# 13. Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
#     Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# n = int(input())
# d = {}
# for i in range (1, n+1):
#     d[i] = (3*i) + 1
# print (d)

# 14 Пользователь задаёт две строки. Определить количество вхождений одной строки в другой.

# string1 = input('Введите строку: ')
# string2 = input('Введите подстроку: ')
# N = string1.count(string2)
# print(N)

# 15. Подсчитать сумму цифр в вещественном числе.

import random


def sum_v(n):
    while n % 2 > 0:
        n *= 10
    sum = 0
    while (n != 0):
        sum = sum + n % 10
        n = n // 10
    print(sum)

# sum_v(12.2345)

# 16. Написать программу получающую набор произведений чисел от 1 до N.
#     Пример: пусть N = 4, тогда
#     [ 1, 2, 6, 24 ]


def proizv(n):
    sum = 1
    result = []
    for i in range(1, n+1):
        sum *= i
        result.append(sum)
    return result

# print (proizv(5))

N = 5
sum = 1
result = []
for i in range(1, N+1):
    sum *= i
    result.append(sum)
print(result)

# 17. Задать список из n чисел последовательности (1+1/n)^n и вывести на экран их сумму


def posled(n):
    ls = []
    d = 0
    sum = 0
    for i in range(1, n+1):
        d = (1+1/i)**i
        ls.append(d)
    for i in ls:
        sum += i
    return round(sum, 2)

# print (posled(9))

# 18. Задать список из N элементов, заполненных числами из [-N, N]. Найти произведение элементов на указанных позициях.
#     Позиции хранятся в файле file.txt в одной строке одно число


def summ(x):
    data = open('file.txt', 'r+')
    res = 1
    for line in data:
        line = int(line)
        if line != 0:
            res *= line
    data.write(f'{str(res)}\n')
    data.close()
    return res


def zapoln(n):
    data = open('file.txt', 'w')
    x = []
    for i in range(-n, n+1):
        data.write(f'{str(i)}\n')
        x.append(i)
    data.close()
    print(x)
    return x


N = 3  # int(input())
# print(summ(zapoln(N)))



# 19. Реализовать алгоритм перемешивания списка.

# lst = list(range(1, 50, 6))
# random.shuffle(lst)
# print(lst)

# 20. Реализовать алгоритм задания случайных чисел. Без использования встроенного генератора псевдослучайных чисел

# import time

# limit = int(input("Введите предел: "))

# rnd_number = str(time.time())
# rnd_number = rnd_number.split(".")
# rnd_number = int(rnd_number[1])

# def random_number(number: int, limit: int):
#     while True:
#         if number > limit:
#             number //= 10
#         else:
#             return number

# print(random_number(rnd_number, limit))
##################################
# the_set = set()

# for i in range(1000):
#     the_set.add(str(i))

# for e in the_set:
#     print(int(e))
#     break

# 21. Определить, присутствует ли в заданном списке строк, некоторое число

def spis_ch(ls, sh):
    spi = []
    for i in ls:
        if sh in i:
            spi.append(i)
    return spi

spisok = ['123ds', '234', '5342', '3231', 'asd21f']
lk = '5'
# print(spis_ch(spisok, lk))


# 22. Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
#     Примеры
#     список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
#     список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
#     список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
#     список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
#     список: [], ищем: "123", ответ: -1

def second_occurrence(ls, fi):
    count = 0
    for i in range(len(ls)):
        if ls[i] == fi:
            count+=1
            if count == 2:
                return i
    return -1

# lt = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
# find = "qwe"
# print(second_occurrence(lt, find))

# 23. Найти сумму чисел списка стоящих на нечетной позиции
#     *Пример:*
#     - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

def sum_odd(spisok):
    count = 0
    result = 0
    for i in range(len(spisok)):
        if count%2 != 0:
            result += spisok[i]
            print(spisok[i], end = ' ')
        count += 1
    return result    

# ls = [2, 3, 5, 9, 3, -2]
# print(f'---> {sum_odd(ls)}')

# 24. Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д. 
#     Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15] 

def PairNum (spisok):
    if len(spisok)%2 == 0:
        num = len(spisok) // 2
    else:
        num = len(spisok) // 2 + 1
    new_spisok = []
    for i in range(num):
        new_spisok.append(spisok[i] * spisok[len(spisok)-1-i])
    return new_spisok

# lst = [2, 3, 4, 5, 6]
# print(PairNum(lst))

# 25. В заданном списке вещественных чисел найдите разницу между максимальным и минимальным значением дробной части элементов. 
#     Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def dif_min_max (spisok):
    for i in range(len(spisok)):
        spisok[i] = spisok[i]%1
    result = max(spisok) - min(spisok)
    return round(result, 2)

# lst = [1.1, 1.2, 3.1, 5, 10.01]
# print (f'{lst} => {dif_min_max(lst)}')

# 26. Написать программу преобразования десятичного числа в двоичное

def Binary(n):
    if(n > 1):
        Binary(n//2)
    print(n%2, end='')

# Binary(int(input('Введите чилсо: ')))

# 27. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#     *Пример:*
#     - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def fib(k):
    if k == 1:
        return 1
    if k == 2:
        return 1
    return (fib(k-1) + fib(k-2))


def neg_fib(k):
    if k == -1:
        return 1
    if k == -2:
        return -1
    return (neg_fib(k+2) - neg_fib(k+1))


def mine_fib(k):
    f = []
    for i in range(-k, 0):
        f.append(neg_fib(i))
    f.append(0)
    for i in range(1, k+1):
        f.append(fib(i))
    return f

# print(mine_fib(int(input('Введите чилсо: '))))

# 28. Строка содержит набор чисел. Показать большее и меньшее число
# Символ-разделитель - пробел
'''
def Max(list1):
    list2 = list(map(int, list1.split()))
    return list2

list1 = input('Введите чилса через пробел: ')
result = Max(list1)
print(min(result), max(result))
'''
# Второй вариант решения через файл
'''
data = 'file.txt'

with open (data, 'r') as f:
    ls = f.readline().split(' ')
    print(ls)

lt = []
for i in ls:
    lt.append(int(i))
print(lt)
print(max(lt))
print(min(lt))
'''

# 29. Найти корни квадратного уравнения Ax² + Bx + C = 0
#     a. Математикой
#     b. Используя дополнительные библиотеки*
'''
path = 'file.txt'
with open(path, 'r') as my_file:
    data = my_file.read()

data = data.split()
print(data)
data = data[:-2]
print(data)
data = [int(data[0][:-3]), int((data[1] + data[2])[:-1]), int(data[3] + data[4])]
print(data)
# D=b^2-4ac
d = data[1]**2 - 4 * data[0] * data[2]
print(d)
# x=((-b(+-))(d^(1/2)))/(2*a))
x_1 = (-data[1] + d**0.5) / (2 * data[0])
x_2 = (-data[1] - d**0.5) / (2 * data[0])
print(x_1, x_2)
'''
# Второй вариант
'''
path = 'file.txt'
with open(path, 'r') as f:
    a = int(f.readline())
    b = int(f.readline())
    c = int(f.readline())

d = b**2 - 4*a*c
print(d)
x_1 = (-b + (d**(1/2)))/(2*a)
x_2 = (-b - (d**(1/2)))/(2*a)
print(round(x_1,2), round(x_2,2))

path = 'file.txt'
with open(path, 'a') as f:
    f.write(f'\nKoren 1: {x_1}')
    f.write(f'\nKoren 2: {x_2}')
'''

# 30. Найти НОК двух чисел
'''
def total_multiple(n1, n2):
    if n1 > n2:
        x = n1
    else:
        x = n2
    while(True):
        if ((x % n1 == 0) and (x % n2 == 0)):
            result = x
            break
        x +=1
    return result

num1 = int(input('Введите число 1: '))
num2 = int(input('Введите число 2: '))
print(total_multiple(num1, num2))
'''

# 31. Вычислить число  c заданной точностью d
# 	Пример: при d = 0.001,  = 3.141. 10-1d10-10

from math import pi

def accuracy(d):
    p = pi 
    count = 0 
    for i in d:
        count+=1
    count-=2
    return round(p, count)

# d = '0.00000000000000000000001'
# print(accuracy(d))

# 32. Составить список простых множителей натурального числа N

def prime_factors(n):
    k = []
    for i in range(1, n+1):
        if n % i == 0: 
            k.append(i)
    return k

# print (prime_factors(int(input('Введите число: '))))