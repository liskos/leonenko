for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                f = (not(w) or z) and ((not(y) or z) == (not(z) or y))
                s = str(x) + str(y) + str(z) + str(w)
                if f:
                    if s.count('1') >= 1:
                        print(y,x,z,w)
