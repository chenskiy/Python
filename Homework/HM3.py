# ## Домашняя работа после Семинара 3
# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#     *Пример:*
#     - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
'''''
spisok = [2, 3, 5, 9, 3, 10, 12, 4, 2, -8]
count = 0
result = 0
for i in range(len(spisok)):
    if count%2 != 0:
        result += i
        print(i, end = ' ')
    count += 1
print()
print(result)
'''''

# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д. 
# Если остается 1 элемент без пары - умножаем его самого на себя.  
#     *Пример:*
#     - [2, 3, 4, 5, 6] => [12, 15, 16];
#     - [2, 3, 5, 6] => [12, 15]
'''''
def PairNum (spisok):
    if len(spisok)%2 == 0:
        num = len(spisok) // 2
    else:
        num = len(spisok) // 2 + 1
    new_spisok = []
    for i in range(num):
        new_spisok.append(spisok[i] * spisok[len(spisok)-1-i])
    return new_spisok
lst = [2, 3, 5, 6]
print(PairNum(lst))
'''''

# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов. 
#     *Пример:*
#     - [1.1, 1.2, 3.1, 5, 10.01] => 0.19


def dif_min_max (spisok):
    for i in range(len(spisok)):
        spisok[i] = spisok[i]%1
    result = max(spisok) - min(spisok)
    result = round(result, 2)
    return result 

lst = [1.03, 1.2, 3.11, 10.12, 12.34]
print (f'{lst} => {dif_min_max(lst)}')
