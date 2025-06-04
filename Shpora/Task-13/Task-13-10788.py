from ipaddress import *

cnt = 0
ip1 = ip_address('201.44.240.33')
ip2 = ip_address('201.44.240.107')

for a in range(5, 31):
    net1 = ip_network(f'{ip1}/{a}', False)
    net2 = ip_network(f'{ip2}/{a}', False)
    if ip1 in net1.hosts() and ip2 in net2.hosts():
        if net1.network_address == net2.network_address:
            cnt += f'{int(net1.network_address):032b}'.count('1') >= 5

print(cnt)