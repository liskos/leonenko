for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                f = (x or not(y)) and not(x == z) and w
                s = str(x) + str(y) + str(z) + str(w)

                if not f and s.count('1') >= 1:
                    print(x,y,z,w)