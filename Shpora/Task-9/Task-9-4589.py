with open('9_4589.txt') as file:
    data = [list(map(int, i.split())) for i in file if i]

def f1(a):
    return max(a) < sum(a) - max(a)

def f2(a):
    return max(a) + min(a) == sum(a) - max(a) - min(a)

cnt = 0

for a in data:
    if f1(a) and f2(a):
        cnt += 1

print(cnt)