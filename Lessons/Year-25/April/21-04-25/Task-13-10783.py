from ipaddress import ip_network, ip_address

ip1 = ip_address('121.171.5.70')
ip2 = ip_address('121.171.5.107')

for a in range(31)[::-1]:
    net1 = ip_network(f'{ip1}/{a}', False)
    if ip1 in net1.hosts() and ip2 in net1.hosts():
        print(net1.num_addresses)
        break