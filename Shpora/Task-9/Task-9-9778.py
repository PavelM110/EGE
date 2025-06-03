with open('09_9778.txt') as file:
    data = [list(map(int, i.split())) for i in file if i]

def f1(a):
    cnt = [a.count(i) for i in set(a)]
    return cnt.count(2) == 1 and cnt.count(1) == 4

def f2(a):
    sr = sum(i for i in a if a.count(i) == 1) / 4
    povt = max(i for i in a if a.count(i) != 1)
    return povt >= sr

for p, i in enumerate(data, start=1):
    if f1(i) and f2(i):
        print(p)
        break