from ipaddress import *

for a in range(16, 25):
    ip = ip_address('246.51.128.202')
    net = ip_network(f'{ip}/{a}', False)
    if ip in net.hosts():
        if all(f'{int(i):032b}'[:16].count('0') <= f'{int(i):032b}'[16:].count('0') for i in net):
            print(a)
            break