f = open('24.txt').readline()
f = f.replace('R', 'Q').replace('W', 'Q')
f = f.replace('2', '1').replace('4', '1')
f = f.replace('QQ', 'Q Q')
f = f.replace('11', '1 1')
a = [x for x in f.split(' ')]
print(len(max(a, key=len)))