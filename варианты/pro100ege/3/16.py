def f(n):
    return g(n-1)
def g(n):
    if n < 10:
        return n
    return g(n-2) + 1
n = [1,4,9,16,25,36,49,64,81,100]
k = 0
for i in range(1, 101):
    if f(i) in n:
        print(i, f(i))
        k+=1
print(k)

