from ipaddress import ip_network
from itertools import product

for a in range(16, 25):
    net = ip_network(f'152.65.245.132/{a}', False)
    if all(f'{int(i):032b}'[:16].count('0') >= f'{int(i):032b}'[16:].count('0') for i in net):
        print(int('1'*(a - 16) + '0'*(8 - (a - 16)), 2))
        break