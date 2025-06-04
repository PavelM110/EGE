from ipaddress import *

net = ip_network('115.192.0.0/255.192.0.0')

cnt = 0

for i in net:
    i = f'{int(i):032b}'
    if i.count('1') % 3 != 0: cnt += 1

print(cnt)