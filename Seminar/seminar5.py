# def myPow(x):
#     return x * x

# # = = = = = =

# def myPow2(x): return x*x


# res1 = myPow(2)
# res2 = myPow2(2)


li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# print(li)
# li2 = []
# for item in li:
#     li2.append(myPow2(item))

# print(li2)

# res = list(map(myPow, li))

# print(res)
f1 = lambda r: r+2 # - не использовать, теряется смысл lambda!!!
res2 = list(map(lambda e: f1(e)**2, li))

print(res2)

