from ipaddress import ip_network, ip_address

for a in range(1, 31)[::-1]:
    ip1 = ip_address('118.187.59.255')
    ip2 = ip_address('118.187.65.115')
    net1 = ip_network(f'118.187.59.255/{a}', False)
    net2 = ip_network(f'118.187.65.115/{a}', False)
    if net1.network_address != net2.network_address:
        if ip1 in net1.hosts():
            if ip2 in net2.hosts():
                break
