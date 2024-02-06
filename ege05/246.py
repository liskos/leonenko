def alg(n):
    n=bin(n)[2:]
    if n.count('0') == n.count('1'):
        n=n+n[-1]
    elif n.count('0') < n.count('1'):
        n+='0'
    elif n.count('1') < n.count('0'):
        n+='1'
    if n.count('0') == n.count('1'):
        n=n+n[-1]
    elif n.count('0') < n.count('1'):
        n+='0'
    elif n.count('1') < n.count('0'):
        n+='1'
    if n.count('0') == n.count('1'):
        n=n+n[-1]
    elif n.count('0') < n.count('1'):
        n+='0'
    elif n.count('1') < n.count('0'):
        n+='1'
    return int(n,2)

for i in range(1, 90):
    if alg(i) % 4 == 0:
        print(i)