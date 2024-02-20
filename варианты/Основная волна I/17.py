import sys
a = [int(x) for x in open('17.txt')]
max_posl = max([x for x in a if (x % 100 == 15)])
k=0
summ=[]
for i in range(1, len(a)-2):
    if ((len(str(a[i])) == 4 and len(str(a[i+1])) != 4 and len(str(a[i+2])) != 4) or (len(str(a[i])) != 4 and len(str(a[i+1])) == 4 and len(str(a[i+2])) != 4) or (len(str(a[i])) != 4 and len(str(a[i+1])) != 4 and len(str(a[i+2])) == 4)) and (a[i]+a[i+1]+a[i+2] >= max_posl):
        k+=1
        summ.append(a[i]+a[i+1]+a[i+2])
print(k, '|', max(summ))