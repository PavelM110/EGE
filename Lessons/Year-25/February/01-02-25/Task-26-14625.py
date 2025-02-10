with open('26_14625.txt') as file:
    n = file.readline()
    k, r, m = list(map(int, file.readline().split()))
    data = [[int(i.split()[0]), int(i.split()[1]), i.split()[-1]] for i in file if i]

m *= 2**20
m1 = m

for i in range(len(data)):
    if data[i][-1] == 'b': data[i][1] = int(data[i][1])
    if data[i][-1] == 'kb': data[i][1] = int(data[i][1]) * 2**10
    if data[i][-1] == 'mb': data[i][1] = int(data[i][1]) * 2**20

data = sorted(data, key=lambda x: -x[1])

types = [r for i in range(k + 1)]
ans = []

for i in data:
    if types[i[0]] > 0:
        types[i[0]] -= 1
        m -= i[1]
        ans.append(i)
    if m <= 0: break

print(len(ans))

t = ans[-1][0]

types[t] += 1

res = m1 - sum([i[1] for i in ans[:-1]])

for i in data[::-1]:
    if i[1] >= res and types[i[0]] > 0:
        print(i[1])
        break