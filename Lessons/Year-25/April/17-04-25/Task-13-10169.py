from ipaddress import ip_network, ip_address

for a in range(1, 33):
    net1 = ip_network(f'157.127.182.76/{a}', 0)
    net2 = ip_network(f'157.127.190.80/{a}', 0)
    if net1.network_address != net2.network_address:
        print(a)
        break