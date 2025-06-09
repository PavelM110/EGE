with open('26_13101.txt') as file:
    n = int(file.readline())
    data = [list(map(int, i.split())) for i in file if i]

data = sorted(data)

windows = [[], []]
cnts = [0, 0]
ans2 = 0

for s, t, n in data:
    for i in range(2):
        for j in windows[i].copy():
            if j <= s: windows[i].remove(j)
    if not n:
        min_cnt = min(len(i) for i in windows)
        if min_cnt >= 14:
            ans2 += 1
            continue
        for i in range(2):
            if len(windows[i]) == min_cnt:
                if len(windows[i]): windows[i].append(max(windows[i]) + t)
                else: windows[i].append(s + t)
                cnts[i] += 1
                break
    else:
        n -= 1
        if len(windows[n]) >= 14:
            ans2 += 1
        else:
            if len(windows[n]): windows[n].append(max(windows[n]) + t)
            else: windows[n].append(s + t)
            cnts[n] += 1

print(max(cnts), ans2)