print('A B C')
for a in 0,1:
    for b in 0,1:
        for c in 0,1:
            f = (a or not(c)) and (not(a) or b or c)# (a  ¬c)  (¬a  b  c)
            if f == 0:
                print(a,b,c)
