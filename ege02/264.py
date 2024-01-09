for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                f = ((w <= z) == y) <= x
                if f == False:
                    print(y,w,z,x, bool(f))