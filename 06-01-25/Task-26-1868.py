with open('26_1868.txt') as file:
    n = file.readline()
    data = [list(map(int, i.split())) for i in file if i]

##data = sorted(data, key=lambda x: (-x[0], x[1]))

list = [[] for i in range(int(n))]

for i in data:
    list[i[0]].append(i[1])

ans_row = 0

for i in list[::-1]:
    k = sorted(i)
    for j in range(len(i) - 1):
        if k[j + 1] - k[j] == 3:
            ans_row = max(ans_row, list.index(i))

ans_list = sorted(list[ans_row])

print(ans_list)

for i in range(len(ans_list) - 1):
    if ans_list[i + 1] - ans_list[i] == 3:
        print(ans_list[i] + 1)
        break