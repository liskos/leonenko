def f(v, x,y,z,w):
    return not(not(w) or (v == x) or (y and not(x))) and not(z)

import itertools
for a in itertools.product([0, 1], repeat=4):
    table = [(a[0], a[1], a[2], 1, 1), (a[0], 1, a[2], 1, 1), (1, a[1], a[2], 1, a[3])]
    for p in itertools.permutations('vxyzw'):
        if len(set(table)) == 3 and [f(**dict(zip(p, t))) for t in table] == [1, 1, 1]:
            print(''.join(p))