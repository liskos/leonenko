# (¬x  y  ¬z  x  ¬y)  ¬w
print('Y X W Z')
for y in 0,1:
    for x in 0,1:
        for w in 0,1:
            for z in 0,1:
                f = (not(x) and y and not(z) or x and not(y)) and not(w)
                if f == 1:
                    print(y,x,w,z)