k=0
for n1 in '12345678':
    for n2 in '012345678':
        for n3 in '012345678':
            for n4 in '012345678':
                for n5 in '012345678':
                    s = n1+n2+n3+n4+n5
                    if s.count('5') == 1 and (n1!=n2 and n2!=n3 and n3!=n4 and n4!=n5):
                        k+=1
print(k)