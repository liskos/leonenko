import sys
sys.stdin = open('24.txt')
s = input()
ss = "XYZ"+'VWXYZ' * 7 + 'VW'
print(ss in s)
print(ss)