for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            f = not(x == (not(y) or z))
            print(x, y, z, f)
