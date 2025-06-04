from ipaddress import *

ip1 = ip_address('121.171.5.70')
ip2 = ip_address('121.171.5.107')

for a in range(30, 0, -1):
    net1 = ip_network(f'{ip1}/{a}', False)
    net2 = ip_network(f'{ip2}/{a}', False)
    if net1.network_address == net2.network_address:
        if ip1 in net1.hosts() and ip2 in net1.hosts():
            print(net1.num_addresses)
            break