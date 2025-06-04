from ipaddress import *

for a in range(16, 25):
    net = ip_network(f'127.63.67.1/{a}', False)
    if ip_address('127.63.67.1') in net.hosts():
        if all(f'{int(i):032b}'[:16].count('1') >= f'{int(i):032b}'[16:].count('1') for i in net):
            print(a)
            break

print(int('11110000', 2))