def f(n):
    n = str(n)
    while ('25' in n) or ('355' in n) or ('5555' in n):
        if '25' in n:
            n = n.replace('25', '33', 1)
        if '355' in n:
            n = n.replace('355', '52', 1)
        if '5555' in n:
            n = n.replace('5555', '2', 1)
    return n
s = set()

for i in range(4, 2001):
    n = '2' + ('5' * i)
    s.add(f(n).count('2'))
print(s)
