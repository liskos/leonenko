for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                s = str(x) + str(y) + str(z) + str(w)
                f1 = (not(x) or  y) or (not(w) == z)
                f2 = (not(x) or  y) == (x and not(z))
                if f1 == f2:
                    print(x,y,z,w)