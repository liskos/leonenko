for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                f = ((not(y) or x) or (not(z) and w)) == (w == x)
                s = str(x) + str(y) + str(z) + str(w)
                if f:
                    if s.count('1') >= 1:
                        print(x,y,w,z)
