with open('9_18134 (1).txt') as file:
    data = [list(map(int, i.split())) for i in file if i]

def f1(a):
    cnt = [a.count(i) for i in set(a)]
    return cnt.count(2) == 2 and cnt.count(1) == 2

def f2(a):
    pov = [i for i in a if a.count(i) > 1]
    nep = [i for i in a if a.count(i) == 1]
    return max(pov) ** 2 > nep[0] * nep[1]

cnt = 0

for i in data:
    if f1(i) and f2(i):
        cnt += 1

print(cnt)