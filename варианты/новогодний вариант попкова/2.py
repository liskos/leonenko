for p in 0,1:
    for y in 0,1:
        for h in 0,1:
            for n in 0,1:
                f = y and not(y or h)  or not(not(y) or h) and (not(n) or p)
                if f:
                    print(p,y,h,n, '|', int(f))