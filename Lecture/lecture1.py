# value = None
# # print(type(value))
# a = 123
# b = 1.23
# # print(type(a))
# # print(type(b))
# value = 12334
# # print(type(value))

# s = 'hello world'

# print(s)   # вывод строки
# print(a, '-' ,b, '-' ,s)
# print('{1} - {2} - {0}'.format(a,b,s))
# print(f'{a} - {b} - {s}')

# f = False
# print(f)

# list = ['1', '2', '3']
# col = ['hello', 1,2,4.5, True]
# print(list)
# print(col)

# print('Введите a');
# a = float(input())
# print('введите b');
# b = float(input())
# print(a, ' + ',b, ' = ', a+b)
# print('{} {}'.format(a, b))
# print(f'{a} {b}')


# a = 1.31231223
# b = 3
# c = round (a * b,7)
# print(c)

# a = 3
# a *= 5

# print(a)

# a = [1,2]
# b = [1,3]
# print (a == b)

# a = 1 < 3 < 5 < 10
# print(a)

# func = 1
# T = 4
# x = 2

# print(func < T > x)


# f = [1,2,3,4]

# print (f)
# print(not 2 in f)

# is_odd = not f[0] % 2
# print(is_odd)


# if if-else

# a = int(input('a = '))
# b = int(input('b = '))
# if a > b:
#     print(a)
# else:
#     print(b)


def f(n):
    n**2
    return n


num = [1, 2, 3, 5, 8, 15, 23, 38]
x = ((num[i], f(num)) for i in num if num[i] % 2 == 0)
print(x)
