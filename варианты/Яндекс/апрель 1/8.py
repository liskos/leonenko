k = 0
for i1 in '123456789ABCDEF':
    for i2 in '0123456789ABCDEF':
        for i3 in '0123456789ABCDEF':
            for i4 in '0123456789ABCDEF':
                for i5 in '0123456789ABCDEF':
                    s = i1 + i2 + i3 + i4 + i5
                    if sum([s.count(i) for i in '0123456789']) == 1 :
                        k = k + 1
print(k)