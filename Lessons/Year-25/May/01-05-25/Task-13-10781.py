from ipaddress import ip_network, ip_address

ip1 = ip_address('112.117.107.70')
ip2 = ip_address('112.117.121.80')

for a in range(1, 31)[::-1]:
    net1 = ip_network(f'{ip1}/{a}', False)
    net2 = ip_network(f'{ip2}/{a}', False)
    if net1.network_address == net2.network_address:
        if ip1 in net1.hosts():
            if ip2 in net1.hosts():
                print(net1.num_addresses)
                break