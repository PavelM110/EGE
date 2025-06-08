with open('26_9793.txt') as file:
    n = int(file.readline())
    shlif = []
    kras = []
    data = []
    for line in file:
        sh, kr = map(int, line.split())
        shlif.append(sh)
        kras.append(kr)
        data.append([sh, kr])


conv = [0] * n

shlif = sorted(shlif)
kras = sorted(kras)

last = 0

for i in range(len(data)):
    sh = shlif[0]
    kr = kras[0]
    if sh < kr:
        for j in range(len(data)):
            s, k = data[j]
            if s == sh:
                kr = k
                last = j + 1
                break
        for j in range(len(conv)):
            if conv[j] == 0:
                conv[j] = last
                break
        shlif.remove(sh)
        kras.remove(kr)
    elif sh > kr:
        for j in range(len(data)):
            s, k = data[j]
            if k == kr:
                sh = s
                last = j + 1
                break
        for j in range(len(conv))[::-1]:
            if conv[j] == 0:
                conv[j] = last
                break
        kras.remove(kr)
        shlif.remove(sh)

print(last, conv.index(last))

with open('26_9793.txt') as file:
    n = int(file.readline())
    data = []
    for num, times in enumerate(file, 1):
        data.append([int(times.split()[0]), 's', num])
        data.append([int(times.split()[1]), 'p', num])

data = sorted(data)

last = 0
conv = [0 for i in range(n)]

for part in data:
    time, type, num = part
    if num not in conv:
        if type == 's':
            last = num
            conv[conv.index(0)] = num
        else:
            lsat = num
            pos = conv[::-1].index(0)
            conv[n - pos - 1] = num

print(last, conv.index(last))