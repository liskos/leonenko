for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                f = (x == (not(y))) <= ((x or z) == w)
                if not f:
                    print(w,z,x,y)