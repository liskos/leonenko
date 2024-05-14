print('X Y Z W V')
for x in 0,1:
    for y in 0,1:
        for z in 0, 1:
            for w in 0, 1:
                for v in 0, 1:
                    f = not(not(w) or (v == x) or (y and not(x))) and not(z)
                    if f:
                        print(v,y,z,w,x)