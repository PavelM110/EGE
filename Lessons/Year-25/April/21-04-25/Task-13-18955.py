from ipaddress import ip_address, ip_network

ip1 = ip_address('200.154.190.12')
ip2 = ip_address('200.154.184.0')

for a in range(32, 0, -1):
    net = ip_network(f'{ip1}/{a}', False)
    if ip1 != net.network_address and ip1 != net.broadcast_address and \
        ip2 in net and ip2 != net.broadcast_address and ip2 != net.network_address:
        print(a)
        break