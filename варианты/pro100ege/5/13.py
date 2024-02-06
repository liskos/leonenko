from ipaddress import *

net=ip_network('136.36.240.16/255.255.255.248', 0)

a = bin(int(ip_address('136.36.240.16')))[2:]
c = list()
for n1 in '01':
    for n2 in '01':
        for n3 in '01':
            s = n1+n2+n3
            b = a[:-3] + s
            if '101' not in b:
                c.append(b)
print(len(c))