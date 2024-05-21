f = open('24.txt').readline()
t = ''
maximum = 0
for i in f:
    t = t + i
    while ('12' in t) or ('21' in t) or ('31' in t) or ('13' in t):
        t = t[1:]
    maximum = max(maximum, len(t))
print(maximum)