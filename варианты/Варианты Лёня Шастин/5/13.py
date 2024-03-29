from ipaddress import *
net = ip_network('192.168.32.48/255.255.255.192', 0)
k = 0
for ip in net:
    if f'{ip:b}'.count('1') % 5 != 0:
        k = k + 1
print(k)