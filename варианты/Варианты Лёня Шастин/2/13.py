from ipaddress import *
net = ip_network('123.222.111.192/255.255.255.248', 0)
s = ''
i = 0
for ip in net:
    ip = [bin(int(x))[2::].zfill(8) for x in str(ip).split('.')]
    if ip[3].count('1') % 3 != 0:
        i = i + 1
print(i)