from fnmatch import *
for i in range(0, 10**10+1, 1917):
    if fnmatch(str(i), '3?12?14*5'):
        print(i, i//1917)