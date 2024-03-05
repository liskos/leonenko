from ipaddress import *
net = ip_network(f'{f}/255.255.255.240', 0)
network_adres = net.network_address
if net.network_address == '192.168.64.176':
    print(ip_address())