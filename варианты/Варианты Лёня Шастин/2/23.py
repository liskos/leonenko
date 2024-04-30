def alg(a,b, k = 0):
    if a == b: return True
    if a > b: return False
    if a < b :
        k = k + 1
        return alg(a+10,b) + alg(a-5,b)
print(f(1,) )