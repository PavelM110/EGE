from ipaddress import *

net = ip_network('192.168.32.48/255.255.255.240')

cnt = 0

for i in net:
    cnt += f'{int(i):032b}'.count('1') % 2

print(cnt)