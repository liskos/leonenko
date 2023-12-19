#  (y  z)  (x  y)
print('X Y Z')
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            f = (not(y) or z) and (not(x) or y)
            if f == 1 or f == 0:
                print(x,y,z, int(f))