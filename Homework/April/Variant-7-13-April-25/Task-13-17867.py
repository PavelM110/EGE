from itertools import product

adress = [172, 16, 168, 0]
mask = [255, 255, 248, 0]

for i in range(len(adress)):
    adress[i] = bin(adress[i])[2:].zfill(8)

for i in range(len(mask)):
    mask[i] = bin(mask[i])[2:].zfill(8)

net = ['', '', '', '']

for i in range(4):
    for j in range(8):
        net[i] += str(int(mask[i][j]) & int(adress[i][j]))

adress = '.'.join(adress)

mask = '.'.join(mask)

net = '.'.join(net)

net_1 = net.count('1')
adress_1 = mask.count('0')

cnt = 0

for i in product([0, 1], repeat=adress_1):
    if (net_1 + i.count(1)) % 5 != 0:
        cnt += 1

print(cnt)

print('A:', adress)
print('M:', mask)
print('N:', net)