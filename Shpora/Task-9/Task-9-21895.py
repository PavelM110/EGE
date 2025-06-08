with open('9_21895.txt') as file:
    data = [list(map(int, i.split())) for i in file if i]

def f1(a):
    return len(a) == len(set(a))

def f2(a):
    a = sorted(a)
    return a[-1] + a[-2] <= sum(a[:3])

cnt = 0

for i in data:
    if f1(i) and f2(i): cnt += 1

print(cnt)