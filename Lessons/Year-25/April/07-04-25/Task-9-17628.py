with open('9_17628 (1).txt') as file:
    data = [list(map(int, i.split())) for i in file if i]

def f(a):
    return min(a) + max(a) <= sum(a) - min(a) - max(a)

cnt = 0

for i in data:
    if f(i):
        cnt += 1

print(cnt)