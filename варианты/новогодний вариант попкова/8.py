k=0
for b1 in 'АГДИЛНРЯ':
    for b2 in 'АГДИЛНРЯ':
        for b3 in 'АГДИЛНРЯ':
            for b4 in 'АГДИЛНРЯ':
                for b5 in 'АГДИЛНРЯ':
                    for b6 in 'АГДИЛНРЯ':
                        s = b1+b2+b3+b4+b5+b6
                        k+=1
                        if s[0] != 'Я' and s.count('Д') == 3 and k%2==0:
                            print(k, s)
