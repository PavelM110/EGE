from ipaddress import ip_network, ip_address

ip = ip_address('192.168.31.80')

net = ip_network(f'{ip}/255.255.255.240')

print(f'{int(net.broadcast_address):032b}'.count('1'))