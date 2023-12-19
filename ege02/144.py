# x  (z  ¬w  y  ¬w  y  ¬z)
print('Y X W Z')
for y in 0,1:
    for x in 0,1:
        for w in 0,1:
            for z in 0,1:
                f = x and (z and not(w) or y and not(w) or y and not(z))
                if f == 1:
                    print(y,x,w,z)