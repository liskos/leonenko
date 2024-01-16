k = 0
j = 0
for b1 in 'ЕИКРСУЯ':
    for b2 in 'ЕИКРСУЯ':
        for b3 in 'ЕИКРСУЯ':
            for b4 in 'ЕИКРСУЯ':
                for b5 in 'ЕИКРСУЯ':
                    for b6 in 'ЕИКРСУЯ':
                        k+=1
                        s = b1+b2+b3+b4+b5+b6
                        if k%2 == 0 and b1 != 'К' and s.count('Е') + s.count('И') + s.count('У') + s.count('Я') <= 2:
                            j+=1
print(j)