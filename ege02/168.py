print('X Y Z W')
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                f = x or (not(y) or z or not(w)) and (y or not(z))
                if f == 0:
                    print(x,y,z,w, int(f))