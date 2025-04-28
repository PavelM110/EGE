with open('9v2.txt') as file:
    data = [list(map(int, i.split())) for i in file]

def f1(a):
    return any(a.count(i) >= 3 for i in a)

def f2(a):
    return any(a.count(i) == 1 for i in a)

def f3(a):
    pov = [i for i in a if a.count(i) > 1]
    nepov = [i for i in a if a.count(i) == 1]
    return sum(pov) / len(pov) < sum(nepov) / len(nepov)

cnt = 0

for i in data:
    if f1(i) and f2(i) and f3(i):
        cnt += 1

print(cnt)