with open('9_19241.txt') as file:
    data = [list(map(int, i.split())) for i in file if i]

def f1(a):
    cnt = [a.count(i) for i in set(a)]
    return cnt.count(3) == 2 and cnt.count(1) == 1

def f2(a):
    pov = [i for i in a if a.count(i) != 1]
    nep = max(i for i in a if a.count(i) == 1)
    return sum(pov) / len(pov) < nep

for p, a in list(enumerate(data, start=1))[::-1]:
    if f1(a) and f2(a):
        print(p)
        break