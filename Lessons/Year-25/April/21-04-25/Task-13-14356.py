from ipaddress import ip_network, ip_address

for a in range(255, -1, -1):
    ip = ip_address(f'217.109.{a}.94')
    net = ip_network(f'{ip}/255.255.254.0', False)
    if ip in net.hosts():
        if all(f'{int(i):032b}'[:16].count('0') <= f'{int(i):032b}'[16:].count('0') for i in net):
            print(a)
            break