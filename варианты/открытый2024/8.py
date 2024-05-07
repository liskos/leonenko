k = 0
for s1 in 'АПРСУ':
    for s2 in 'АПРСУ':
        for s3 in 'АПРСУ':
            for s4 in 'АПРСУ':
                for s5 in 'АПРСУ':
                    k = k + 1
                    s = s1+s2+s3+s4+s5
                    if (s.count('У') <= 1) and ('АА' not in s):
                        print(k)