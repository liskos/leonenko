for A in range(0, 1000):
    if all([not(x&A != 0) or (not((x&17 == 0) and (x&5 == 0)) or (x&3!=0)) for x in range(0, 1000)]):
        print(A)

