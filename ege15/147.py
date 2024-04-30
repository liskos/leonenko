s = set()
for i1 in '01':
    for i2 in '01':
        for i3 in '01':
            for i4 in '01':
                for i5 in '01':
                    for i6 in '01':
                        for i7 in '01':
                            for i8 in '01':
                                s.add(i1+i2+i3+i4+i5+i6+i7+i8)

p = {i for i in s if i[:2] == '11'}
q = {i for i in s if i[-1] == '0'}

def f(a):
    for x in s:
        ff = (x in a) or ((x not in p) or (x in q))
        if not ff: return False
    return True

a = s.copy()
for i in s:
    a.remove(i)
    if not f(a):
        a.add(i)

print(a, '|', len(a))
