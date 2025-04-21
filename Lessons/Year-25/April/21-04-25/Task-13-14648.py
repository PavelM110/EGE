from ipaddress import ip_network, ip_address

for a in range(33):
    net = ip_network(f'218.48.192.56/{a}', False)
    if net.network_address == ip_address('218.48.192.0'):
        if net.num_addresses - 2 >= 500:
            print(net.netmask)