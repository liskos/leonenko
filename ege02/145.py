# x  (y  z  y  ¬w  ¬z  ¬w)
print('Y X W Z')
for y in 0,1:
    for x in 0,1:
        for w in 0,1:
            for z in 0,1:
                f = x and (y and z or y and not(w) or not(z) and not(w))
                if f == 1:
                    print(y,x,w,z)