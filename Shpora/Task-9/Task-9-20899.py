with open('9_20899.txt') as file:
    data = [list(map(int, i.split())) for i in file if i]

def f1(a):
    return max(a) < sum(a) - max(a)

def f2(a):
    cnt = 0
    a = sorted(a)
    for i in range(len(a) - 1):
        cnt += a[i] == a[i+1]
    return cnt == 1

cnt = 0

for i in data:
    if f1(i) and f2(i):
        cnt += 1

print(cnt)