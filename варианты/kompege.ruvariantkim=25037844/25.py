def pr(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


print(pr(1))
for i in range(670001, 670100):
    a = []
    for j in range(1,i):
        if i % j == 0:
            if pr(j):
                a.append(j)
    if sum(a) % 10 == 5:
        print(i, sum(a))