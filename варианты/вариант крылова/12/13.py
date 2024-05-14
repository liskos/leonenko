from ipaddress import *


for a in range(0, 256):
    ip = f'64.129.{a}.10'
    net = ip_network(f'{ip}/255.255.252.0', 0)
    b = 0
    if all(f'{ip:b}'[:16].count('1') <= f'{ip:b}'[16::].count('1') for ip in net):
        print(a)



