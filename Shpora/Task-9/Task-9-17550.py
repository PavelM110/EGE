with open('09_17550.txt') as file:
    data = [list(map(int, i.split())) for i in file if i]

def f1(a):
    cnt = [a.count(i) for i in set(a)]
    return cnt.count(3) == 1 and cnt.count(1) == 3

def f2(a):
    povt = sum(i for i in a if a.count(i) > 1) ** 2
    nep = sum(i for i in a if a.count(i) == 1) ** 2
    return povt > nep

cnt = 0

for i in data:
    if f1(i) and f2(i): cnt += 1

print(cnt)