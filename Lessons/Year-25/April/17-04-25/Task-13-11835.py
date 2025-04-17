from ipaddress import ip_network

cnt = 0

for a in range(256):
    net = ip_network(f'207.0.{a}.167/255.255.255.192', False)
    if all(f'{int(i):032b}'[:16].count('0') > f'{int(i):032b}'[16:].count('0') for i in net):
        cnt += 1

print(cnt)