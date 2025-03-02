with open('26.txt') as file:
    n = int(file.readline())
    duels = [list(map(int, i.split())) for i in file if i]

# for i in range(len(duels)):
#     duels[i] = (duels[i][0], duels[i][0] + duels[i][1])

duels = sorted(duels, key=lambda x: (x[1] + x[0], x[0]))

accepted = [duels[0]]

for duel in duels:
    if duel[0] >= accepted[-1][1] + accepted[-1][0]: accepted.append(duel)

print(len(accepted), accepted[-1][0] - (accepted[-2][1] + accepted[-2][0]))

print(accepted)

print(sorted(duels, key=lambda x: x[0])[-20:])