print('X Y Z W')
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                f = not(x) and y and (not(w) or z)
                if f:
                    print(x,y,z,w, int(f))

