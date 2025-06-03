with open('9_12241 (1).txt') as file:
    data = [list(map(int, i.split())) for i in file if i]

def f1(a):
    cnt = [a.count(i) for i in set(a)]
    return cnt.count(2) == 3 and cnt.count(1) == 1

def f2(a):
    pov = [i for i in a if a.count(i) != 1]
    nep = max(i for i in a if a.count(i) == 1)
    return (max(pov) + min(pov)) / 2 < nep

cnt = 0

for a in data:
    cnt += f1(a) and f2(a)

print(cnt)