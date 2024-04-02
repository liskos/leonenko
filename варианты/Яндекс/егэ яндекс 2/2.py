for a in 0,1:
    for b in 0,1:
        for c in 0,1:
            for d in 0,1:
                f = (not((a and b)) or c) and (not(b and c) or d)
                if not f:
                    print(d,b,a,c)