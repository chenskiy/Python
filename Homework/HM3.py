# ## Домашняя работа после Семинара 3
# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
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



# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д. 
# Если остается 1 элемент без пары - умножаем его самого на себя.  
#     *Пример:*
#     - [2, 3, 4, 5, 6] => [12, 15, 16];
#     - [2, 3, 5, 6] => [12, 15]

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



# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов. 
#     *Пример:*
#     - [1.1, 1.2, 3.1, 5, 10.01] => 0.19


def dif_min_max (spisok):
    for i in range(len(spisok)):
        spisok[i] = spisok[i]%1
    result = max(spisok) - min(spisok)
    return round(result, 2)

# lst = [1.1, 1.2, 3.1, 5, 10.01]
# print (f'{lst} => {dif_min_max(lst)}')



# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#     *Пример:*
#     - 45 -> 101101
#     - 3 -> 11
#     - 2 -> 10

def Binary(n):
    if(n > 1):
        Binary(n//2)
    print(n%2, end='')

# Binary(int(input('Введите чилсо: ')))



# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
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