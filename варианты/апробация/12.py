def alg(n):
    while ('1111' in n) or ('8888' in n):
        if '1111' in n:
            n = n.replace('1111', '8', 1)
        else:
            n = n.replace('8888', '11', 1)
    return n
print(alg('8' * 82))