s=set()
def alg(n):
    n=bin(n)[2:]

    return int(n[:-2],2)

for i in range(20,601):
    s.add(alg(i))
print(len(s))