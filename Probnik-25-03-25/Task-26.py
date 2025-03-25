with open('2600.txt') as file:
    n = int(file.readline())
    data = [(int(i.split()[0]), int(i.split()[0]) + int(int(i.split()[1]) / 10) + 1, int(i.split()[1])) for i in file if i]

data = sorted(data, key=lambda x: (x[1], x[0]))

conf = [data[0]]

for i in data:
    if i[0] >= conf[-1][1]:
        conf.append(i)

print(len(conf), sum(i[-1] for i in conf))