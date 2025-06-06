from encodings.idna import ace_prefix

with open('26_10107.txt') as file:
    n = int(file.readline())
    data = [list(map(int, i.split())) for i in file if i]

data = sorted(data, key=lambda x: [x[1], x[0]])

accepted = [data[0][1]]

for s, e in data:
    if s >= accepted[-1]:
        accepted.append(e)

accepted = accepted[:-1]

for s, e in sorted(data, key=lambda x:[-x[0], x[1]]):
    if s >= accepted[-1]:
        print(len(accepted) + 1, s - accepted[-1])
        break