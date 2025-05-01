from ipaddress import ip_network, ip_address

ip = ip_address('238.51.1.202')

for a in range(16, 25):
    net = ip_network(f'{ip}/{a}', False)
    if ip in net.hosts():
        if all(f'{int(i):032b}'[:16].count('1') >= f'{int(i):032b}'[16:].count('1') for i in net):
            print(net.netmask)
            break