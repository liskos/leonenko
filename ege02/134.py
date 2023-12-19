for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            f = (not(x) and z) or (not(x) and not(y) and not(z))# (¬x  z)  (¬x  ¬y  ¬z)
            if f == 1:
                print(x,y,z)