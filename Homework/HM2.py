## Домашняя работа Семинара 2
# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр(отсекаем минус, считаем все в плюс).
#     *Пример:*
#     - 67,82 -> 23
#     - 0,56 -> 11

def summ(num):
    sum = 0
    for i in num:
        if i != '.' and i != '-' and i != 0:
            sum += int(i)
    return(sum)

# print(summ(input('Введите вещественное число: ')))



# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#     *Пример:*
#     - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def products_numbers(N):
    result = 1
    ls = []
    for i in range(1, N+1):
        result *= int(i)
        ls.append(result)
    return ls

# print(products_numbers(int(input('Введите число: '))))



# 3. Задать список из n чисел последовательности (1+1/n)^n и вывести на экран их сумму

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

# print(posled(int(input('Введите число: '))))



# 4. Задать список из N элементов, заполненных числами из [-N, N]. Найти произведение элементов на указанных позициях.
#    Позиции хранятся в файле file.txt в одной строке одно число

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

# N = 3  # int(input())
# print(summ(zapoln(N)))



# 5. Реализуйте случайное перемешивания списка.
#    *Пример:*
#    Исходный вариант -> ['Веселый пианист', 250, 3.14, 'True ']
#    Результат -> [250, 3.14, 'True ', 'Веселый пианист']

import random
def shuf_col(col): 
    print(f'Исходный вариант --> {col}')
    random.shuffle(col)
    print(f'Результат --> {col}')

# txt = ['Веселый пианист', 250, 3.14, 'True ']
# shuf_col(txt)