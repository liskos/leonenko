k = 0
for s1 in 'ВЗГЛЯД':
    for s2 in 'ВЗГЛЯД':
        for s3 in 'ВЗГЛЯД':
            for s4 in 'ВЗГЛЯД':
                s = s1+s2+s3+s4
                if 1 <= s.count('З') <= 2:
                    k+=1
print(k)