for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                f1 = (not(w) or z) == (not(y) or x)
                f2 = (not(w) or z) and (not(x) == y)
                s = str(x) + str(y) + str(z) + str(w)
                if (s.count('1') >= 2 and s.count('0') >= 1) and f2 == False:
                    print(x,y,z,w, '|', int(f1), int(f2))
