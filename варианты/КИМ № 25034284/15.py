for x in range(0,100):
    for y in range(0,100):
        for a in range(0,100):
            f = (x**2 + y**2 > 1024 - x) or (y < -2*x + a)
            if f == True:
                print(a)
                break