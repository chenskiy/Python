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

def random_coef(k):
    from random import randint
    random_coef_list = [randint(0,101) for i in range(k+1)]
    return random_coef_list


def polinom(list_arg):
    k = len(list_arg) - 1
    result_list = [str(list_arg[i])+'*x**'+str(k-i) for i in range(k-1) if list_arg[i] != 0]
    if list_arg[k-1] != 0:
        result_list.append(str(list_arg[k-1])+'*x')
    if list_arg[k] != 0:
        result_list.append(str(list_arg[k])) 
    result = ' + '.join(result_list) + ' = 0'
    return result


k = int(input("Введите показатель степени многочлена: "))
with open('file.txt', 'w') as data:
    data.write(polinom(random_coef(k)))

# 35. Даны два файла в каждом из которых находится запись многочлена. Сформировать файл содержащий сумму многочленов.