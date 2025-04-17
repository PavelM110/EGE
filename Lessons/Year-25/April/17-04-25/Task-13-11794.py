from ipaddress import ip_network

for a in range(256)[::-1]:
    net = ip_network(f'223.167.{a}.167/26', False)
    if all(f'{int(j):032b}'[:16].count('0') <= f'{int(j):032b}'[16:].count('0') for j in net):
        print(a)
        break
