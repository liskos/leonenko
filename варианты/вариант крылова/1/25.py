from fnmatch import *
for i in range(0, 10**10 + 1, 31007):
    if fnmatch(str(i), '1*34?5?9'):
        print(str(i), int(i / 31007))