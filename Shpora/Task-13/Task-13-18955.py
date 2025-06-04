from ipaddress import *

ip1 = ip_address('200.154.190.12')
ip2 = ip_address('200.154.184.0')

for a in range(30, 9, -1):
    net = ip_network(f'{ip1}/{a}', False)
    if ip2 in net.hosts() and ip1 in net.hosts():
        print(a)
        break