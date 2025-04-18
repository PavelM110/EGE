with open('9_21408.txt') as file:
    data = [list(map(int, i.split())) for i in file if i]

def f1(a):
    cnt = [a.count(i) for i in set(a)]
    return cnt.count(3) == 2 and cnt.count(1) == 1

def f2(a):
    max_p = max(i for i in a if a.count(i) > 1)
    nep = max(i for i in a if a.count(i) == 1)
    return max_p > nep

cnt = 0

for i in data:
    if f1(i) and f2(i):
        cnt += 1

print(cnt)
