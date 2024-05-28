def alg(n):
    while ('?1' in n) or ('?2' in n) or ('?3' in n):
        if ('?1' in n):
            n = n.replace('?1', '123?', 1)
        if ('?2' in n):
            n = n.replace('?2', '4?1', 1)
        if ('?3' in n):
            n = n.replace('?3', '2?12', 1)
    return n
s = alg('?' + 302 * '1' + 109 * '2' + 224 * '3')
b = sum([int(i) for i in s[:-1]])
print(b)