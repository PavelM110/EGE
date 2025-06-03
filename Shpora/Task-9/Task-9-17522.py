with open('9_17522 (1).txt') as file:
    data = [list(map(int, i.split())) for i in file if i]

def f1(a):
    return max(a) < sum(a) - max(a)

def f2(a):
    return len(set(a)) == len(a) - 1

cnt = 0

for a in data:
    cnt += f1(a) and f2(a)

print(cnt)