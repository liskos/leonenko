for x in 0,1:
    for y in 0,1:
        for w in 0,1:
            for z in 0,1:
                f = not(x == (w and not(z))) and (y == (x and not(w)))
                if f:
                    print(w,x,y,z)