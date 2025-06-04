from ipaddress import *

cnt = 0

for a in range(0, 256):
    ip = ip_address(f'246.81.65.{a}')
    net = ip_network(f'{ip}/255.255.255.224', False)
    if ip in net.hosts():
        if all(f'{int(i):032b}'[16:24].count('0') > f'{int(i):032b}'[24:].count('0') for i in net.hosts()):
            cnt += 1

print(cnt)