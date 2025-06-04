from ipaddress import *

net = ip_network('112.160.0.0/255.240.0.0')

cnt = 0

for i in net:
    cnt += f'{int(i):032b}'.count('1') % 3 != 0

print(cnt)