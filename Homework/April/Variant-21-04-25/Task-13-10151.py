from ipaddress import ip_network, ip_address

for a in range(1, 33):
    net = ip_network(f'111.81.208.27/{a}', False)
    if net.network_address == ip_address('111.81.192.0'):
        print(net.netmask)
        break