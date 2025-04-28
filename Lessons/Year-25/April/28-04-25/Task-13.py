from ipaddress import ip_network, ip_address

net = ip_network('79.128.96.0/255.255.224.0')

cnt = 0

for i in net:
    i = f'{int(i):032b}'
    if i.count('1') % 7 != 0:
        if i[-3:] == '100':
            cnt += 1

print(cnt)