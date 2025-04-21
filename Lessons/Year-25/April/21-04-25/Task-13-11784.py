from ipaddress import ip_network


for a in range(256)[::-1]:
    net = ip_network(f'248.112.{a}.35/255.255.255.240', False)
    if all(f'{int(i):032b}'[:16].count('0') <= f'{int(i):032b}'[16:].count('0') for i in net):
        print(a)
        break