with open('26_19752.txt') as file:
    n = int(file.readline())
    data = []
    for i in file:
        player = list(map(int, i.split()))
        summ = sum(player[1:])
        pluses = sum(i for i in player[1:] if i > 0)
        anses = sum(1 for i in player[1:] if i != 0)
        data.append([summ, pluses, anses, player[0]])

data = [i for i in data if i[0] > 0]
data = sorted(data, key=lambda x: [-x[0], -x[1], -x[2], x[3]])

next_tour = data[:len(data) // 3]

for i in data:
    if i not in next_tour:
        if i[:-1] == next_tour[-1][:-1]:
            next_tour.append(i)

for i in next_tour: data.remove(i)

dop_next_tour = data[:int(len(data) * .1)]

for i in data:
    if i not in dop_next_tour:
        if i[:-1] == dop_next_tour[-1][:-1]:
            dop_next_tour.append(i)

print(dop_next_tour[0], len(dop_next_tour))