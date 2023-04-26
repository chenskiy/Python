# # Домашняя работа Семинара 4

# 1. Вычислить число c заданной точностью d
#     Пример:
#     - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

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

# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def prime_factors(n):
    k = []
    for i in range(1, n+1):
        if n % i == 0: 
            k.append(i)
    return k

# print (prime_factors(int(input('Введите число: '))))

# 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

def non_repeating(n):
    ls = []
    for i in n:
        if i not in ls:
            ls.append(i)
    return(ls)

# numbers = [1, 2, 3, 5, 1, 5, 3, 10]
# print(non_repeating(numbers))


# 4.  Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
#     Пример:
#     - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random
print('\n-----4 задача-----\n')
def rand(k): 
    r = []
    for i in range(k + 1):
        i = random.randint(0,101)
        r.append(i)
    return r

def assembling(r):  #заполняем строку многочленами
    st = ''
    for i in range(len(r)-1, -1, -1):
        if r[i] > 1:
            if i == 0:
                st += str(r[i]) + ' + '
            elif i == 1:
                st += str(r[i]) + 'x' + ' + '
            else:
                st += str(r[i]) + 'x^' + str(i) + ' + '
        elif r[i] == 1:
            if i == 0:
                st += ' + '
            elif i == 1:
                st += 'x' + ' + '
            else:
                st += 'x^' + str(i) + ' + '          
    st = st[:-3]
    st += ' = 0'
    return st

k = int(input("Введите натуральную степень: ")) 
r = rand(k) 
print(f'{r} - Сформированый случайным образом список коэффициентов')
a = assembling(r)
print(f'{a} - записаный в файл многочлен в степени {k}')
data = 'Task4.txt'              #Запись пойдет также в 5 задачу
with open(data, 'w') as f_1:
    f_1.write(a)


# 5. Даны два файла в каждом из которых находится запись многочлена. Сформировать файл содержащий сумму многочленов.

print('\n-----5 задача-----\n')


def pure_polynomials(a):       # Отделение коэффициентов 
    a = a[:-3]
    a = a.replace(' ', '').replace('^', '').split('+')
    c = ''
    b = []
    for i in range(len(a)):
        c = ''
        for j in a[i]:
            if j != 'x':
                c += str(j)
            else: break
        c = int(c)
        b.append(c)
    return b

def summ(f1, f2):   # суммируем коэф. многочлена
    sum=[]
    for i in range(len(f1)):
        sum.append(f1[i] + f2[i])
    return sum

r = rand(k) 
print(f'{r} - Сформированый случайным образом список(2) коэффициентов')
a = assembling(r)
print(f'{a} - записаный в файл(2) многочлен в степени {k}\n')

path = 'Task5.txt'              
with open(path, 'w') as f_2:
    f_2.write(a)

with open(data, 'r') as f_1:
    f_1 = f_1.readline()

with open(path, 'r') as f_2:
    f_2 = f_2.readline()

ppf_1 = pure_polynomials(f_1)
ppf_2 = pure_polynomials(f_2)

print(f'{ppf_1} коэффициенты многочлена из 1-го файла')
print(f'{ppf_2} коэффициенты многочлена из 2-го файла')

s = summ(ppf_1, ppf_2)
print(f'{s} сумма коэф. многочленов\n')

assemb = assembling(s)
print(f'{assemb} Сформирован файл(3) содержащий сумму многочленов\n')

dpat = 'Task5(end).txt'
with open(dpat, 'w') as f_3:
    f_3.write(assemb)