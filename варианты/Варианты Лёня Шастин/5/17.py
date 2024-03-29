x = [int(x) for x in open('17.txt')]
minimim = min([int(x) for x in open('17.txt') if abs(int(x)) % 100 == 25]) # -88625
k = 0
s = set()
for i in range(6676):
    if (x[i] * x[i+1] * x[i+2] <= minimim**2) and ((len(str(x[i])) == 4) + (len(str(x[i+1])) == 4) + (len(str(x[i+2])) == 4)) == 2:
        k = k + 1
        s.add(x[i] * x[i+1] * x[i+2])
print(k, min(s))