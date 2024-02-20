h = set()
for s1 in 'ГИПЕРБОЛА':
    for s2 in 'ГИПЕРБОЛА':
        for s3 in 'ГИПЕРБОЛА':
            for s4 in 'ГИПЕРБОЛА':
                for s5 in 'ГИПЕРБОЛА':
                    for s6 in 'ГИПЕРБОЛА':
                        s=s1+s2+s3+s4+s5+s6
                        ss = s.replace('И','1').replace('Е', '1').replace('О', '1').replace('А','1')
                        ss = ss.replace('Г','2').replace('П', '2').replace('Р', '2').replace('Б','2').replace('Л','2')
                        if (ss[0] == '2') and (ss[-1] == '2') and ('212' not in ss):
                            h.add(s)
print(len(h))
