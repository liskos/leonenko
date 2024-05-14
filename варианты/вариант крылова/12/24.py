f = open('24.txt').readline()
t = ''
maximum = 0
for i in f:
    t = t + i
    if ('12' not in t) and ('21' not in t) and ('31' not in t) and ('13' not in t):
        maximum = max(maximum, len(t))
    else:
        t = ''
print(maximum)