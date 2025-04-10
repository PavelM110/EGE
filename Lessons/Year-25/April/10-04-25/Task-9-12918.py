with open('9_12918.txt')as file:
    data = [list(map(int, i.split())) for i in file if i]

def f1(a):
    cnt = [a.count(i) for i in set(a)]
    return cnt.count(2) == 2 and cnt.count(1) == 2

def f2(a):
    return a.count(max(a)) == 1

def f3(a):
     u = max(a) * min(a) > sum(a) - min(a) - max(a)
     return u

for i in data:
    if f1(i) and f2(i) and f3(i):
        print(sum(i))
        break