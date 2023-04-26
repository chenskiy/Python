from audioop import reverse
from turtle import title


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
    x = 'a,e,i,o,u'
    count = 0
    for i in x:
        if (i in sentence):
            print(i)
            count += sentence.count(i)
    return count

def getCount(s):
    return sum(c in 'aeiou' for c in s)


def disemvowel(string_):
    x = 'AEIOUaeiou'
    for i in x:
        string_ = string_.replace(i, '')
    return string_

def square_digits(num):
    res = ''
    for i in str(num):
        res += str(int(i)**2)
    return res

def high_and_low(numbers):
    numbers = numbers.split()
    ls = []
    for i in numbers:
        ls.append(int(i))
    
    return f'{max(ls)} {min(ls)}'

def descending_order(num):
    return ''.join(sorted(str(num), reverse=True))

def solution(number):
    return sum(i for i in range(1,number) if i%3==0 or i%5 == 0)

def even_or_odd(number):
    return 'Even' if number%2 == 0 else 'Odd'

def accum(s):
    return "-".join([s[i].upper() + (s[i].lower() * i) for i in range(len(s))])

def is_square(n):    
    return n > -1 and ((n**0.5) % 1) == 0

def get_middle(s):
    return s[int((len(s)-1)/2):-int((len(s)-1)/2)] if len(s) > 2 else s

def positive_sum(arr):
    return sum(i for i in arr if i>0)

def filter_list(l):
    return [i for i in l if not(type(i) is str)]

def is_isogram(s):
    return len(set(s.lower())) == len(s.lower())

def xo(s):
    return s.lower().count('x') == s.lower().count('o')


def to_jaden_case(string):
    return ' '.join(i.capitalize() for i in string.split())

def spin_words(sentence):
    return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])

def find_it(seq):
    return max(i for i in seq if seq.count(i)%2!=0)

def digital_root(n):
    ls = []
    while n > 0:
        ls.append(n%10)
        n = n//10
        if n <= 0:
            n = sum(i for i in ls)
            ls = []
            if n < 10: break 
    return n
    # return n if n < 10 else digital_root(sum(map(int,str(n))))

def array_diff(a, b):
    return [i for i in a if not(i in b)]

print(array_diff([1,2,2], [2]))
