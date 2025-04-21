from ipaddress import ip_network, ip_address

ip = ip_address('143.131.211.37')

for a in range(31)[::-1]:
    net = ip_network(f'{ip}/{a}', False)
    if ip in net.hosts():
        cnt = 0
        for i in net:
            if f'{int(i):032b}'.count('1') == 10:
                cnt += 1
        if cnt == 15:
            print(a)
            break