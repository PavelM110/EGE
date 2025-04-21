from ipaddress import ip_network, ip_address

cnt = 0

for a in range(256):
    net = ip_network(f'246.81.65.{a}/255.255.255.224', False)
    ip = ip_address(f'246.81.65.{a}')
    if ip != net.broadcast_address and ip != net.network_address:
        if all(f'{int(i):032b}'[17:25].count('0') > f'{int(i):032b}'[25:].count('0') for i in net.hosts()):
            cnt += 1

print(cnt)