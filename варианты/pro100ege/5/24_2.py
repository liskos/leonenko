import sys
sys.stdin = open('24.txt')
s = input()
ss = "VWXYZ"
while ss in s:
    ss += 'VWXYZ'
print(ss)
while ss not in s:
    ss = ss[1:]
ss += "VWXYZ"
print(ss)
while ss not in s:
    ss = ss[:-1]
print(ss)
print(len(ss))
