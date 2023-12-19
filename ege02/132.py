print('A B C')
for a in 0,1:
    for b in 0,1:
        for c in 0,1:
            f = not((not(a) or b)) or (not(a) and c)# (a  b)  (¬a  c)
            if f == 0:
                print(a,b,c)