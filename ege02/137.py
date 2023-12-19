print('Y X W Z')
for y in 0,1:
    for x in 0,1:
        for w in 0,1:
            for z in 0,1:
                f = x and not(w) and (y or not(z))
                if f == 1:
                    print(y,x,w,z)