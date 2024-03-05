s = set()
for x in range(0, 1000):
    for A in range(0, 1000):
        f = not(int(bin(x)[2:])&int(bin(A)[2:]) != 0) or (not((int(bin(x)[2:])&17 == 0) and (int(bin(x)[2:])&5 == 0)) or (int(bin(x)[2:])&3!=0))
        if f:
            s.add(A)
print(max(s))

