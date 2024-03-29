k = 0
for s1 in 'АЗИМНОПРТ':
    for s2 in 'АЗИМНОПРТ':
        for s3 in 'АЗИМНОПРТ':
            for s4 in 'АЗИМНОПРТ':
                for s5 in 'АЗИМНОПРТ':
                    s = s1+s2+s3+s4+s5
                    k = k + 1
                    if (k % 2 == 0) and s[0] == 'Н' and s.count('Р') == 2:
                        print(k)