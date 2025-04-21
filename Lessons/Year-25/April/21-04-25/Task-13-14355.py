from ipaddress import ip_network

for a in range(16, 25):
    net = ip_network(f'127.63.67.1/{a}', False)
    if all(f'{int(i):032b}'[:16].count('1') >= f'{int(i):032b}'[16:].count('1') for i in net):
        print(net.netmask)
        break