f = 16**820 - 2**761 + 14
def schisl(f):
    s = ''
    while f > 0:
        s = s + str(f % 4)
        f = f // 4
    return s[::-1]
print(schisl(f).count('0'))
