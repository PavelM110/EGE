from ipaddress import ip_address, ip_network

for a in range(33)[::-1]:
    net = ip_network(f'211.115.61.154/{a}', False)
    ip = ip_address('211.115.59.137')
    if ip in net:
        print(net.netmask)
        break