def f(x, y, z, w):
    return not(not(x) or z) or (y == w) or y


import itertools
for a in itertools.product([0,1], repeat=4):
    table = [(1,0,a[2],a[3]), (a[0], 1, 0, a[3]), (0, a[1], a[2], a[3])]
    for p in itertools.permutations('xyzw'):
        if [f(**dict(zip(p, t))) for t in table] == [0,0,0]:
            print("".join(p))