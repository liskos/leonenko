p = range(25*10, 50*10+1)
q = range(32*10, 47*10+1)

def alg(A):
    for x in range(-100, 500):
        f = not((x in A) or not(x in p)) or (not(x in A) or (x in q))
        if not f:
            return False
    return True

print(alg(range(32*10,47*10+1)))





