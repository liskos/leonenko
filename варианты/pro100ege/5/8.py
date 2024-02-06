k=0
for b1 in 'ПРОСТ':
    for b2 in 'ПРОСТ':
        for b3 in 'ПРОСТ':
            for b4 in 'ПРОСТ':
                for b5 in 'ПРОСТ':
                    for b6 in 'ПРОСТ':
                        s=b1+b2+b3+b4+b5+b6
                        if len(set(s)) == 5 and s.count('О') == 2 and (s[0] != s[1]) and (s[1] != s[2]) and (s[2] != s[3]) and (s[3] != s[4]) and (s[4] != s[5]):
                            k+=1
print(k)