with open('input.txt') as file:
    n = file.readline()
    data = [list(map(int, i.split())) for i in file if i]

data = sorted(data)

ids = [[] for i in range(49995)]

for idi, num in data:
    if num not in ids[idi]:
        ids[idi] = sorted(ids[idi] + [num])

print(data.index(max(data, key=len)))