from ipaddress import ip_network, ip_address

for a in range(33)[::-1]:
    net = ip_network(f'112.117.107.70/{a}', False)
    ip = ip_address('112.117.121.80')
    if ip in net:
        print(net.netmask)
        break