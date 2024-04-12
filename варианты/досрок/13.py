from ipaddress import *
net = ip_network('105.224.200.224/255.255.255.224', 0)
k = 0
for ip in net:
    s = ''
    a = str(ip).split('.')
    for x in a:
        n = bin(int(x))[2:]
        s = s + n
    if s.count('1') % 4 == 0:
        k = k+1
print(k)
