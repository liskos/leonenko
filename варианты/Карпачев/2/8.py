k = 0
for s1 in 'АБВКУ':
    for s2 in 'АБВКУ':
        for s3 in 'АБВКУ':
            for s4 in 'АБВКУ':
                for s5 in 'АБВКУ':
                    for s6 in 'АБВКУ':
                        for s7 in 'АБВКУ':
                            s = s1+s2+s3+s4+s5+s6+s7
                            s = s.replace('А', '1').replace('У', '1').replace('Б', '2').replace('В','2').replace('К','2')
                            k = k + 1
                            if ('11' not in s) and ('22' not in s):
                                print(k, '|', s)