k=0
for s1 in 'АГМНСТУ':
    for s2 in 'АГМНСТУ':
        for s3 in 'АГМНСТУ':
            for s4 in 'АГМНСТУ':
                for s5 in 'АГМНСТУ':
                    for s6 in 'АГМНСТУ':
                        s = s1+s2+s3+s4+s5+s6
                        k+=1
                        if s[0]!='У' and (s.count('М')==2) and (s.count('Г') <= 1):
                           print(k)