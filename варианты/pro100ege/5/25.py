for i in range(1, 200):
    x = (i *1012) ** 2
    x = str(x)
    if x[0] == '1' and x[2] == '2' and x[-1] == '4' and int(x) <= 10**10:
        print(x, int(x)//2024)