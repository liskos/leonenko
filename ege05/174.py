s=set()
def alg(n):
    n=bin(n)[2:].zfill(8)
    answer = '1' * n.count('1')
    return int(answer,2)

for i in range(10,2501):
    s.add(alg(i))
print(len(s))