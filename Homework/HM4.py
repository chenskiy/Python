# # Домашняя работа Семинара 4

# 1. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#     *Пример:*
#     - 45 -> 101101
#     - 3 -> 11
#     - 2 -> 10
'''
def Binary(n):
    if(n > 1):
        Binary(n//2)
    print(n%2, end='')

n = int(input('Введите чилсо: '))
Binary(n)
'''
# 2. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#     *Пример:*
#     - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
'''

def Fib(k):
    if k == 1:
        return 1
    if k == 2:
        return 1
    return (Fib(k-1) + Fib(k-2))


def NegFib(k):
    if k == -1:
        return 1
    if k == -2:
        return -1
    return (NegFib(k+2) - NegFib(k+1))


k = int(input('Введите чилсо: '))
f = []
for i in range(-k, 0):
    f.append(NegFib(i))
f.append(0)
for i in range(1, k+1):
    f.append(Fib(i))
print(f)
'''

# 3. Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число. В качестве символа-разделителя используйте пробел.

'''
def Max(list1):
    list2 = list(map(int, list1.split()))
    return list2


list1 = input('Введите чилса через пробел: ')
result = Max(list1)
print(min(result), max(result))
'''

# 4. Задайте два целых числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.

'''
def TotalMultiple(n1, n2):
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
print(TotalMultiple(num1, num2))
'''
