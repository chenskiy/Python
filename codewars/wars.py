from audioop import reverse


def derive(coefficient, exponent):
    a = coefficient*exponent
    b = exponent - 1
    return f'{a}x^{b}'

def cockroach_speed(s):
    return int(s*100000/3600)

def nearest_sq(n):
    
    return (round(n**0.5)**2)

def find_next_square(sq):
    if sq <= 0:
        return -1    
    sq = sq**0.5
    print(sq)
    if (sq%int(sq)) == 0:
        sq += 1
        return int(sq**2)
    else:
        return -1

# def Bianry(k):
#     ls = ''
#     while k > 0:
#         ls += (str(k%2))
#         k = k//2
#     ls = ls[::-1]
#     ls = int(ls)
#     # if ls % 2 == 0:

#     return int(ls)

def baum_sweet():
    ls = []
    while k > 0:
        ls.append(k%2)    
        k = k//2

    return ls

def solution(string, ending):
    return string.endswith(ending)
# print(solution('abce', 'e'))

import string
def words_to_marks(s):
    x = 0
    values = dict()
    for index, letter in enumerate(string.ascii_lowercase):
        values[letter] = index + 1
    # return values

    for i in s:
        x += int(values[i])
    return x


def words_to_marks(s):
    return sum('_abcdefghijklmnopqrstuvwxyz'.index(e) for e in s)

# def get_count(sentence):
#     x = 'a, e, i, o, u'
#     count = 0
#     ls = []
#     lt = []
#     for i in x:
#         if not(i in sentence) and 'y' in sentence:
#             return 0
#         if i in sentence:
#             ls.append(i)
#     for j in ls:
#         if j not in lt:
#             lt.append(i) 
#     return len(lt)
# print(get_count('abracadabra'))

def get_count(sentence):
    x = 'a, e, i, o, u'
    count = 0
    for i in x:
        if not(i in sentence) and 'y' in sentence:
            return 0
        if i in sentence:
            count += 1
    return count

print(get_count('abracadabra'))