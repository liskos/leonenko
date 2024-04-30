f = [int(x) for x in open('17_11703.txt')]
maximum = max([int(x) for x in f if str(x)[-2:] == '18']) # 99360
s = []
for i in range(len(f)-2):
    if (len(str(abs(f[i]))) == 5 or len(str(abs(f[i+1]))) == 5 or len(str(abs(f[i+2]))) == 5) and ((f[i] * f[i+1] * f[i+2]) % maximum == 0):
        s.append(f[i] * f[i+1] * f[i+2])
print(len(s), max(s))