# my_list = [1, 2, 3, 456, 896, 0, 2, 3]
# m = [x for x in my_list if my_list.count(x) < 2]

# print(m)


# listt = [1,23,543,23,4,5,6,7]
# x = [i for i in listt if listt.count(i) == 1]
# print(x)

lst = [1,23,543,23,4,5,6,7]
y = list(filter(lambda x: lst.count(x) == 1, lst))
print(y)