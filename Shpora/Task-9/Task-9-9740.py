with open('9_9740.txt') as file:
    data = [list(map(int, i.split())) for i in file if i]

def f1(a):
    cnt = [a.count(i) for i in set(a)]
    return cnt.count(3) == 1 and cnt.count(1) == 4

def f2(a):
    pov = [i for i in a if a.count(i) != 1]
    nep = [i for i in a if a.count(i) == 1]
    return sum(nep) / len(nep) <= sum(pov) / len(pov)

cnt = 0

for a in data:
    cnt += f1(a) and f2(a)

print(cnt)