def alg(n):
    a = []
    b = bin(n)[2:]
    if b.count('1') > b.count('0'):
        b+='0'
    else:
        b+='1'
    if len(b) % 2 == 0:
        b=b[:len(b)//2 - 1] + b[(len(b)//2) + 1:]
    else:
        b = b[:len(b)//2 -1] + b[(len(b)//2)+2:]
    return int(b,2)

k=0
s = set()
for i in range(5, 1000):
    if 50<= alg(i) <= 100:
        s.add(alg(i))
print(len(s))