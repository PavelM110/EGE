from ipaddress import ip_network, ip_address

for a in range(33)[::-1]:
    net = ip_network(f'153.202.16.37/{a}', False)
    if ip_address('153.202.16.37') in net.hosts():
        if net.network_address == ip_address('153.202.16.32'):
            print(net.netmask)
            break