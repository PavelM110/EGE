from ipaddress import ip_network

for a in range(256):
    net = ip_network(f'192.214.{a}.184/255.255.255.224', False)
    if all(f'{int(i):032b}'.count('1') > 15 for i in net):
        print(a)
        break