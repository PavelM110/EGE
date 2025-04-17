from ipaddress import ip_network
from itertools import product

a_list = [int(''.join(i), 2) for i in product('01', repeat=8) if '01' not in ''.join(i)]

for a in a_list:
    net = ip_network(f'152.65.245.132/255.255.{a}.0', False)
    if all(f'{int(i):032b}'[:16].count('0') >= f'{int(i):032b}'[17:].count('0') for i in net):
        print(a)
        break