print('X Y Z W')
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                f = not(not(x) or not(not(z) or w)) and (not(not(z)) or (not(w) == y))
                s = str(x) + str(y) + str(z) + str(w)
                if (s.count('1') >= 3 and f == 0) or (s.count('0') >= 2 and f == 1) or (s.count('0') >= 2 and f == 1):
                    print(x,y,z,w, f)