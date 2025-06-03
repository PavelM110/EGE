with open('9_16375 (1).txt') as file:
    data = [list(map(int, i.split())) for i in file if i]

def f1(a):
    cnt = [a.count(i) for i in set(a)]
    return cnt.count(2) == 1 and cnt.count(1) == 5

def f2(a):
    pov = max(i for i in a if a.count(i) != 1)
    nep = sorted([i for i in a if a.count(i) == 1])
    return nep[0] * nep[1] * nep[2] > pov**2

cnt = 0

for a in data:
    cnt += f1(a) and f2(a)

print(cnt)