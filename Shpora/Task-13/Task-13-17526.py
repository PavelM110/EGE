from ipaddress import *

net = ip_network('172.16.128.0/255.255.192.0')

cnt = 0

for i in net:
    cnt += f'{int(i):032b}'.count('1') % 2

print(cnt)