f = (5 * 3**1917) + (6*2**1878) + (7*3**1870) - 1991
def g(f):
    s = ''
    while f > 0:
        j = f % 17
        if j == 10:
            s+='A'
        if j == 11:
            s+='B'
        if j == 12:
            s+='C'
        if j == 13:
            s+='D'
        if j == 14:
            s+='E'
        if j == 15:
            s+='F'
        if j == 16:
            s+='G'
        if j <= 9:
            s+=str(j)
        f = f // 17
    return s

for i in range(0,10):
    print(g(f).count(str(i)), i)