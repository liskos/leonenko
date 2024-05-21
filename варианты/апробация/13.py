from ipaddress import *
net = ip_network('122.159.136.144/255.255.255.248', 0)
k = 0
for ip in net:
    b = f'{ip:b}'
    if b.count('1') % 4 != 0:
        k = k + 1
print(k)