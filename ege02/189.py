for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                f = (x and z) or ((not(w) or x) == (not(z) or y))
                if not f:
                    print(x,y,z,w )
