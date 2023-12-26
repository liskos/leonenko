for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                f = (not(y) or x or z) and (not(z) or y)
                s = str(x) + str(y) + str(z) + str(w)
                if not f:
                    if s.count('1') >= 1:
                        print(z,y,x,w)
