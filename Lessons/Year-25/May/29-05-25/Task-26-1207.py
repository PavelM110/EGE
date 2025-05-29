with open('26_1207.txt') as file:
    s, n = map(int, file.readline().split())
    data = [int(i) for i in file if i]

data = sorted(data)

saved = []

for i in data:
    if sum(saved) + i <= s:
        saved.append(i)
    else:
        break

saved = saved[:-1]

for i in sorted(data, reverse=True):
    if sum(saved) + i <= s:
        print(len(saved) + 1, i)
        break