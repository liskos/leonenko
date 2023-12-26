for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                f = not((x or not(z))) or ((x and w) == y)
                if not f:
                    print(y,x,z,w)
