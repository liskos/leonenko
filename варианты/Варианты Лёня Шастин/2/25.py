from fnmatch import *

for i in range(21025, 10**10+1, 21025):
    i = str(i)
    b = i.replace('1', '-').replace('3', '-').replace('5', '-').replace('7', '-').replace('9', '-').replace('2','+').replace('4', '+').replace('6', '+').replace('8', '+')
    if fnmatch(i, '12*34?5') and (int(i) % 21025 == 0) and b.count('+') == b.count('-'):
        print(i, int(i)/21025)