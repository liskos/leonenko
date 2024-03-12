for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                f = not(not(x) or y) or (x == z) or w
                if not f:
                    print(x,w,z,y)