# 32. Составить список простых множителей натурального числа N

    # number = int(input("введите число: "))
    # k = [i for i in range(1, number+1) if(number % i == 0)]
    # print(k)

# 33. Дана последовательность чисел. Получить список неповторяющихся элементов исходной последовательности
#     Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]

# numbers = [1, 2, 3, 5, 1, 5, 3, 10]
# unique_numbers = list(set(numbers))
# print(unique_numbers)

# 34. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
#     *Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

def rand(k): 
    r = []
    for i in range(k + 1):
        i = random.randint(0,101)
        r.append(i)
    return r

def assembling(r):
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
print(r)
a = assembling(r)
print(a)


# 35. Даны два файла в каждом из которых находится запись многочлена. Сформировать файл содержащий сумму многочленов.

a = a[:-3]
a = a.replace(' ', '').replace('^', '').split('+')
print(a)
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
print(a)
print(b)