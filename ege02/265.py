for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                f = ((x or y) == (y <= z)) or w
                if f == False:
                    print(x,y,z,w, bool(f))