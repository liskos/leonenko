print('Y X W Z')
for y in 0,1:
    for x in 0,1:
        for w in 0,1:
            for z in 0,1:
                f = not(y) and x and (not(z) or w)# ¬y  x  (¬z  w)
                if f == 1:
                    print(y,x,w,z)