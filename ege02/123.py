for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            f = (not(x) or y or z) and (not(x) or not(y) or z) and (x or not(y) or not(z))
            if f == 0:
                print(x,y,z)