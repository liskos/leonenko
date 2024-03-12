for A in range(1, 1000):
    if all( (((4* x + y) < A) or (x < y) or (22 <= x)) for x in range(1, 1000) for y in range(1,1000)):
        print(A)