from ipaddress import ip_network

for a in range(1, 33)[::-1]:
    net1 = ip_network(f'121.171.5.70/{a}', False)
    net2 = ip_network(f'121.171.5.107/{a}', False)
    if net1.network_address == net2.network_address:
        print(net1.num_addresses)
        break