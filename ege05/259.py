def alg(n):
    n=[n for n in bin(n)[2:]]
    if n[-1]=='0':
        n[-1] = n[0] + n[1]
    else:
        return ''
    n=''.join(n)[::-1]
    return int(n, 2)
for i in range(1, 1000):
    if alg(i) == 119:
        print(i)