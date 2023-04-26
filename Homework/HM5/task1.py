# 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

def comprehension(w, c):
    w = w.split()
    print(w)
    k = [i for i in w if c not in i]
    return k

char = 'абв'
word = 'абв Ура, питон круто, очеагбвнь инетресные семинарабвы! абв'

print(comprehension(word, char))