from ipaddress import ip_address, ip_network

ip_net = ip_address('143.172.8.0')
ip = ip_address('143.172.12.114')

for a in range(16, 25):
    net = ip_network(f'{ip}/{a}', False)
    if net.network_address == ip_net:
        if ip != net.broadcast_address and ip != net.network_address:
            print(net.netmask)
            break