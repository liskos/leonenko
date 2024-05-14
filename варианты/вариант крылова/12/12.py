def f(n):
    while ('11111' in n) or ('15' in n):
        if '11111' in n:
            n = n.replace('11111', '15', 1)
        else:
            n = n.replace('15', '1', 1)
    return n
print(f('1' * 65))