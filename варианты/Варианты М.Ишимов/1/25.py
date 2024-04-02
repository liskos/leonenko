from fnmatch import *
k = 0
for i in range(0, 10**10, 2919):
    if fnmatch(str(i), '9*253?74'):
        k+=1
        print(i, i // 2919)