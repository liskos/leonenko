n = 0
k = 0
for s1 in 'АВИОРТФ':
    for s2 in 'АВИОРТФ':
        for s3 in 'АВИОРТФ':
            for s4 in 'АВИОРТФ':
                for s5 in 'АВИОРТФ':
                    for s6 in 'АВИОРТФ':
                        s = s1 + s2 + s3 + s4 + s5 + s6
                        n = n + 1
                        if n % 2 == 0 and s[0] != 'О' and s.count('Р') == 2:
                            k = k + 1
print(k)
