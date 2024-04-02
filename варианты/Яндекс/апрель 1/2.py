for x in 0,1:
    for y in 0,1:
        for w in 0,1:
            f = (x and (not(w) or y)) == 1
            print(x,y,w, '|', int(f))
