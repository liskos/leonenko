p = {2,4,6,8,10,12,14,16,18,20}
q = {5,10,15,20,25,30,35,40,45,50}

def alg(a):
    for x in range(1, 1000):
        f = (not(x in a) or (x in p)) and (not(x in q) or not(x in a))
        if not f:
            return False
    return True

m = 0
for x in range(1, 300):
    for y in range(x, 300):
        s = range(x,y)
        if alg(s):
            print(s)