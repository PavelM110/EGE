with open('9_6897.txt') as file:
    data = [list(map(int, i.split())) for i in file if i]


def f1(a):
    return max(a) < sum(a) - max(a)


def f2(a):
    return min(a) + max(a) != sum(a) - min(a) - max(a)


cnt = 0

for i in data:
    if f1(i) and f2(i):
        cnt += 1

print(cnt)
