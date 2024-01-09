for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                s = str(x) + str(y) + str(z) + str(w)
                f = (x and y) or (y == z) or w
                if not f:
                    print(z,y,w,x)