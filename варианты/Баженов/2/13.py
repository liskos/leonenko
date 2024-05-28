from ipaddress import *
net = ip_network('157.128.0.0/255.224.0.0', 0)
s = []
for ip in net.hosts():
    s.append(f'{ip:b}'.count('0'))
print(min(s))
