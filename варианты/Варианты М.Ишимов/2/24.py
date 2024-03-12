import sys
sys.stdin = open('24.txt')
a = input()
for i in '23456789':
    a = a.replace(i, '1')
m = 0
t = ""
for i in a:
    if i == '1':
        t += i
        m = max(len(t), m)
    elif t == '' and i == '+':
        continue
    elif i == '+' and t[-1]=="1":
        t += i
    elif i == '+' and t[-1] == '+':
        t = ''

print(m)
