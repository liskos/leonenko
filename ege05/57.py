for i in range(1000, 10000):
    a1, a2, a3, a4 = str(i)
    s1 = int(a1) + int(a2)
    s2 = int(a3) + int(a4)
    s = str(max(s1,s2)) + str(min(s1,s2))
    if s == '1412':
        print(i)