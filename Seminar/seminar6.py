# my_list = [1, 2, 3, 456, 896, 0, 2, 3]
# m = [x for x in my_list if my_list.count(x) < 2]

# print(m)


# listt = [1,23,543,23,4,5,6,7]
# x = [i for i in listt if listt.count(i) == 1]
# print(x)

# lst = [1,23,543,23,4,5,6,7]
# y = list(filter(lambda x: lst.count(x) == 1, lst))
# print(y)

def main_fun(value):
    name = value
    def second():
        print('Hello', name)
    return second()

# main_fun('Igor')

def adder(value):
    def inner(a):
        return value*a
    return inner

# a2 = adder(2)

# print(a2(3))

def counter():
    count = 0
    def inner():
        nonlocal count
        count+=1
        return count
    # print(count)
    return inner


# q = counter()
# print(q())

# def average_numbers():
#     summa = 0
#     count = 0
#     def inner(num):
#         nonlocal summa
#         nonlocal count
#         summa += num
#         count += 1
       
#         return summa/count

#     return inner

# r1 = average_numbers()
# # print(r1(5),r1(10), r1(20))

# from datetime import datetime

# def timer():
#     start = datetime.now()
#     def inner():
#         return datetime.now() - start
#     return inner

# t = timer()
# print(t())
# print(t())


# def header(func):
#     def inner(*args, **kwargs):
#         print('<h1>')
#         func(*args, **kwargs)
#         print('<\h1>')

#     return inner


def table(func):
    def inner(*args, **kwargs):
        print('<table>')
        func(*args, **kwargs)
        print('</table>')

    return inner


@table
def say(name, surname, age):
    print('hello', name, surname, age)

def sqr(x):
    """
    Функция возводит в квадрат x
    """
