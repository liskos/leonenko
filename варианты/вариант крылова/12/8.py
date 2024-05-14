# АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ
k = 0
for s1 in 'АВИКЛ':
    for s2 in 'АВИКЛ':
        for s3 in 'АВИКЛ':
            for s4 in 'АВИКЛ':
                for s5 in 'АВИКЛ':
                    for s6 in 'АВИКЛ':
                        s = s1+s2+s3+s4+s5+s6
                        k = k + 1
                        if (s.count('А') <= 2) and (s.count('В') == 2) and (s.count('И') == 0) and ('И' not in s):
                            print(k)