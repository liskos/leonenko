import sys
sys.stdin = open('26.txt')
a = [list(map(int, input().split())) for _ in range(1000)]
a = [[i[0], i[0]+i[1]] for i in a]
c = [] #  отобранные мероприятия
b = a[:] #  мероприятия, на которые можно успеть
while b:
    b = sorted(b, key=lambda x: x[1])
    c.append(b[0])
    b.pop(0)
    d = b[:]
    b = [i for i in b if i[0] >= c[-1][1]]
print(len(c))
print(c)
print(d)
print(max(d, key=lambda x: x[0]))