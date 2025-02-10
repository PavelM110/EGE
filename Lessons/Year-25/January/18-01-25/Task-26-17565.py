with open('26_17565.txt') as file:
    n, s = map(int, file.readline().split())
    data = [list(map(int, i.split())) for i in file if i]

data_sum = [[i[0], sum(i[1:-1]), i[-1]] for i in data]

data_sum = sorted(data_sum, key=lambda x: (-x[1], -x[2], x[0]))

prohod = data_sum[:s]

cnt = 0

half_prohod = prohod[-1][1]

for i in range(s)[::-1]:
    if prohod[i][1] != half_prohod:
        print(prohod[i])
        break

for i in data_sum:
    if i[1] == half_prohod:
        cnt += 1

print(cnt)


# prohod = data_sum[:s]
#
# if prohod[-1][1] == data_sum[s][1]:
#     while prohod[-1][1] == data_sum[s][1]:
#         prohod = prohod[:-1]
#
# half_prohod = [i for i in data_sum if i[1] == data_sum[s][1]]
#
# prohod = sorted(prohod, key=lambda x: (-x[1], -x[-1], -x[0]))
#
# print(len(half_prohod))
#
# print(prohod[-1][0])