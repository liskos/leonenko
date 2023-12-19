# (¬x  y  z  x  ¬z)  ¬w
print('Y X W Z')
for y in 0,1:
    for x in 0,1:
        for w in 0,1:
            for z in 0,1:
                f = (not(x) and y and z or x and not(z)) and not(w)
                if f == 1:
                    print(y,x,w,z)