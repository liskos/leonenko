for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                f = (not (x) and (not(z) or y) and not(w)) or ((z == w) and (not(x or y) or w))
                if f:
                    print(x,y,z,w)