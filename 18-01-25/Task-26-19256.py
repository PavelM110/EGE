with open('26_19256.txt') as file:
    n = file.readline()
    data = [list(map(int, i.split())) for i in file if i]

data = sorted(data)

tasks = [[] for i in range(50_000)]

cnts = [[] for i in range(50_000)]

for i in data:
    tasks[i[0]].append(i[1])

for i in range(len(tasks)):
    tasks[i] = list(set(tasks[i]))

