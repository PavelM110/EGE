with open('26_20970 (1).txt') as file:
    n, k = map(int, file.readline().split())
    data = [list(map(int, i.split())) for i in file if i]

data = sorted(data)

fixers = [[] for i in range(k + 1)]
cnts = [0 for i in range(k + 1)]
ans2 = 0

for s, t, n in data:
    for p in range(1, k + 1):
        for i in fixers[p].copy():
            if i <= s: fixers[p].remove(i)
    if not n:
        min_cnt = min([len(i) for i in fixers])
        if min_cnt >= 5:
            ans2 += 1
            continue
        for p in range(1, k + 1):
            if len(fixers[p]) == min_cnt:
                if len(fixers[p]): fixers[p].append(max(fixers[p])+ t)
                else: fixers[p].append(s + t)
                cnts[p] += 1
                break
    else:
        if len(fixers[n]) < 5:
            cnts[n] += 1
            if len(fixers[n]):
                fixers[n].append(max(fixers[n]) + t)
            else:
                fixers[n].append(s + t)
        else:
            ans2 += 1


print(max(cnts), ans2)