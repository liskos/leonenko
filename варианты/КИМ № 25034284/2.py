for y in 0,1:
    for z in 0,1:
        for w in 0,1:
            for x in 0,1:
                f = (not((x and not(y))) or (z and w)) and ((not(y) or z) or (not(w) or x))
                if not f:
                    print(y,z,w,x)