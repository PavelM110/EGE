from sys import flags

with open('26_10107.txt') as file:
    n = int(file.readline())
    data = [list(map(int, i.split())) for i in file if i]

data = sorted(data, key=lambda x: (x[1]))

events = [data[0]]

flag = True

while flag:
    flag = False
    for i in data:
        if i[0] >= events[-1][1]:
            events.append(i)
            flag = True
            break

print(len(events))

for i in sorted(data, key=lambda x: -x[0]):
    if i[0] >= events[-2][1]:
        print(i[0] - events[-2][1])
        break
