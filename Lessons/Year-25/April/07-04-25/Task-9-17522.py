with open('9_17522.txt') as file:
    data = [list(map(int, i.split())) for i in file if i]

def f1(a):
    return max(a) < sum(a) - max(a)

def f2(a):
    return len(set(a)) == 3

cnt = 0

for i in data:
    if f1(i) and f2(i):
        cnt += 1

print(cnt)