for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            fow w in 0,1:
                f = not(w) and (y or not(z) or not(x) and y)
                s = str(x) + str(y) + str(z)
                if not f:
                    if s.count('1') >= 1:
                        print(z,y,x,w)