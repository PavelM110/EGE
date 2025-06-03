with open('9_17628 (1).txt') as file:
    data = [list(map(int, i.split())) for i in file if i]

cnt = 0

for a in data:
    cnt += max(a) + min(a) <= sum(a) - max(a) - min(a)

print(cnt)