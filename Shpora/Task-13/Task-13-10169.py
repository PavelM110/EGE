from ipaddress import *

ip1 = ip_address('157.127.182.76')
ip2 = ip_address('157.127.190.80')

for a in range(10, 31):
    net1 = ip_network(f'{ip1}/{a}', False)
    net2 = ip_network(f'{ip2}/{a}', False)
    if net1.network_address != net2.network_address:
        if ip1 in net1.hosts() and ip2 in net2.hosts():
            print(a)
            break