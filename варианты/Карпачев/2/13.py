from ipaddress import *
net = ip_network('145.139.8.0/255.255.128.0', 0)
k = 0
for ip in net:
    if (ip.packed[0].__format__('b').count('1') + ip.packed[1].__format__('b').count('1') >
            3 * (ip.packed[2].__format__('b').count('1') + ip.packed[3].__format__('b').count('1'))):
        k = k + 1
print(k)
for ip in net:
    print(ip.__format__("b"))