from random import randint

def bot_play(cell):
    while True:
        num = randint(0, 8)
        if cell[num] == '':
            cell[num] = '0'
            print(f'{cell[0]:^5}|{cell[1]:^5}|{cell[2]:^5}')
            print(f'-----------------')
            print(f'{cell[3]:^5}|{cell[4]:^5}|{cell[5]:^5}')
            print(f'-----------------')
            print(f'{cell[6]:^5}|{cell[7]:^5}|{cell[8]:^5}')
            return num

def human_play(cell):
    while True:
        num = int(input('Введите ячейку: '))
        if cell[num] == '':
            cell[num] = 'X'
            print(f'{cell[0]:^5}|{cell[1]:^5}|{cell[2]:^5}')
            print(f'-----------------')
            print(f'{cell[3]:^5}|{cell[4]:^5}|{cell[5]:^5}')
            print(f'-----------------')
            print(f'{cell[6]:^5}|{cell[7]:^5}|{cell[8]:^5}')
            return num


def human_vs_bot(game):
    human = []
    bot = []
    cell = ['' for x in range(9)]
    win_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    while game:
        human.append(human_play(cell))    
        print(human)
        lenn = len(human)
        if lenn >= 3:
            variations = [(i, j, k) for i in human for j in human for k in human]
            for elemnt in variations:
                if elemnt in win_combinations:
                    game = False
                    return 'Human Win'
        if game:
            bot.append(bot_play(cell))
            print(bot)
            ln = len(bot)
            if ln >= 3:
                variations_bot = [(i, j, k) for i in bot for j in bot for k in bot]
                for belement in variations_bot:
                    if belement in win_combinations:
                        game = False
                        return 'Bot Win'
            

print(f'\n{human_vs_bot(True)}\n')