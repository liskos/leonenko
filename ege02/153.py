# (x  z)  ( y  x)
print('X Y Z')
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            f = (not(x) or not(z)) and (not(y) or x)
            print(x,y,z, int(f))