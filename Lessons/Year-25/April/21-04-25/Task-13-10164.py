from ipaddress import ip_address, ip_network

ip = ip_address('156.132.15.138')

net = ip_network(f'{ip}/255.255.252.0', False)

print(list(net.hosts()).index(ip) + 1)