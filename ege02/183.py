print('X Y Z')
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            f = (not(y) or x) and z and not(z == y)
            if f == 1:
                print(x,y,z, int(f))