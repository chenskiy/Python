# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: 
# На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
#     a) Добавьте игру против бота
#     b) Подумайте как наделить бота ""интеллектом""

import random

def player_human(c):
    # p = random.randint(1,28)      # На случай если лень играть
    # print('Human to take: ')
    p = 0
    while p > 28 or p < 1:
        p = int(input('Human to take 1...28: '))
        if p > 28 or p < 1:
            print('Неправильно введены данные')
    c -= p
    print(c)
    return(p)

def player_bot(c):
    while c > 1000:
        if c%29 != 0:
            p = c%29
        else: 
            p = random.randint(1,28)
        print(f'Bot to take: {p}')
        c -= p
        print(c)
        return(p)
    if c%29 != 0:
        p = c%29
    else: 
        p = random.randint(1,28)
    print(f'Bot to take: {p}')
    c -= p
    print(c)
    return(p)

def battle (candies):
    flag = random.randint(0,2)
    if flag == 1:
        print('Первым ходит кожаный')
        while candies >= 0:
            if candies > 0:
                human = player_human(candies)
                candies -= human
            if candies == 0: 
                return ('Human Win')
            if candies > 0:
                bot = player_bot(candies)
                candies -= bot
            if candies == 0: 
                return ('Bot Win')
    else:
        print('Первым ходит бот')
        while candies >= 0:
            if candies > 0:
                bot = player_bot(candies)
                candies -= bot
            if candies == 0: 
                return ('Bot Win')
            if candies > 0:
                human = player_human(candies)
                candies -= human
            if candies == 0: 
                return ('Human Win')

print(battle(2021))