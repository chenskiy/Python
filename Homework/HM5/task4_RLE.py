def compres(file): 
    result = '' 
    prev_char = '' 
    count = 1
    for i in range(1, len(file)): 
        if file[i-1] != file[i]:
            prev_char = file[i-1]
            result += str(count) + prev_char
            count = 1          
        else:
            count+=1
            e = file[i]
    result += str(count) + e
    return result

def recov(txt):
    num = ''
    res = ''
    for i in range(len(txt)):
        if txt[i].isdigit():
            num += txt[i]
        else:
            res += txt[i] * int(num)
            num = ''
    return res

data = 'compression.txt'
path = 'recovery.txt'

with open(data, 'r') as c:
    c = c.readline()
print(c)

com = compres(c)
print(compres(c))

with open(path, 'w') as w:
    w.write(com)

with open(path, 'r') as r:
    r = r.readline()

rec = recov(r)
print(rec)