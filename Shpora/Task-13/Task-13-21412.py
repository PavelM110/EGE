from ipaddress import *

ip = ip_address('143.168.72.213')

net = ip_network(f'{ip}/255.255.255.240', False)

print(max(net.hosts()))