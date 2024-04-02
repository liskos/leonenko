from ipaddress import *
for A in range(1, 256):
    net = ip_network(f'{int('11110110',2)}.{int('01010001',2)}.{int('01000001',2)}.{int(A, 2)}/255.255.255.224', 0)
