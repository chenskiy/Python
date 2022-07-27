my_list = [1, 2, 3, 456, 896, 0, 2, 3]
m = [x for x in my_list if my_list.count(x) < 2]

print(m)
