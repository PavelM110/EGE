from ipaddress import ip_network

for a in range(1, 33):
    net1 = ip_network(f'193.175.175.231/{a}', False)
    net2 = ip_network(f'193.175.176.118/{a}', False)
    if net1.network_address != net2.network_address:
        print(net1.netmask)
        break