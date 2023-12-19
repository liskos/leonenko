print('A B C')
for a in 0,1:
    for b in 0,1:
        for c in 0,1:
            f = (not(a) or b) and (not((a and b)) or not(c)) #(a  b)  ((a  b)  ¬c).
            if f == 0:
                print(a,b,c)