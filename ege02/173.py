print('X Y Z W')
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                f = x or (z and not(w)) or (y and not(w)) or (y and not(z))
                if f == 0:
                    print(x,z,y,w, int(f))