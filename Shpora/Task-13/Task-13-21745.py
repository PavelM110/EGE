from ipaddress import *

ip1 = ip_address('95.24.2.9')
ip2 = ip_address('95.24.3.10')

ans = 0

for a in range(10, 31):
    net1 = ip_network(f'{ip1}/{a}', False)
    net2 = ip_network(f'{ip2}/{a}', False)
    if net1.network_address != net2.network_address:
        if ip1 in net1.hosts() and ip2 in net2.hosts():
            cnt1 = sum([1 for i in net1.hosts() if f'{int(i):032b}'[-1] == '0'])
            cnt2 = sum([1 for i in net2.hosts() if f'{int(i):032b}'[-1] == '0'])
            ans = max(ans, cnt1, cnt2)

print(ans)