from ipaddress import *
#1
k=0
for a in range(256):
    net = ip_network(f'207.0.{a}.167/255.255.255.192', 0)
    if all(f'{ip:b}'[:16].count('0') > f'{ip:b}'[16:].count('0') for ip in net):
        k+=1
print(k)



