k = 0
c = 0
for s1 in 'АГИЛМОРФ':
    for s2 in 'АГИЛМОРФ':
        for s3 in 'АГИЛМОРФ':
            for s4 in 'АГИЛМОРФ':
                for s5 in 'АГИЛМОРФ':
                    s = s1+s2+s3+s4+s5
                    k+=1
                    if s1 + s2 != 'ЛМ'  and s.count('И') >= 2 and (k % 2 == 0):
                        c += 1
print(c)