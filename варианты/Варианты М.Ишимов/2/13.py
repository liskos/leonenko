from ipaddress import *
for A in range(255):
    net = ip_network(f'154.127.{A}.230/255.255.255.192', 0)
    if all()