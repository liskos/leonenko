for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                f = (not(y)) and (x <= ((not(z)) == w)) or z
                if f == False:
                    print(x,y,w,z, bool(f))