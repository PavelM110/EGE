from ipaddress import ip_address, ip_network

ip1 = ip_address('123.20.103.136')
ip2 = ip_address('123.20.103.151')

for a in range(33):
    net1 = ip_network(f'{ip1}/{a}', False)
    net2 = ip_network(f'{ip2}/{a}', False)
    if net1.network_address != net2.network_address:
        if ip1 != net1.broadcast_address and ip1 != net1.network_address and \
            ip2 != net2.broadcast_address and ip2 != net2.network_address:
            print(net1.netmask)