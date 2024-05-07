from ipaddress import *
net = ip_network('122.159.136.144/255.255.255.248', 0)

for ip in net:
    ip = [bin(int(s))[2:].zfill(8) for s in str(ip).split('.')]
    s = ip[0] + ip[1] + ip[2] + ip[3]
    if s.count('1') % 4 != 0:
        print(s)