for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                s = str(x) + str(y) + str(z) + str(w)
                f = ((x <= y) or (z == x)) and (w <= z)
                if s.count('1') == 2 and s.count('0') == 2 and f == True:
                    print(x,y,z,w, '|', f)
                if s.count('0') == 3 and f == False:
                    print(x,y,z,w, '|', f)
                if s.count('1') == 3 and f == False:
                    print(x,y,z,w, '|', f)