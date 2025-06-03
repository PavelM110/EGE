with open('9_9832.txt') as file:
    data = [list(map(int, i.split())) for i in file if i]

def f1(a):
    cnt = [a.count(i) for i in set(a)]
    return cnt.count(2) == 2 and cnt.count(1) == 3

def f2(a):
    return a.count(max(a)) == 1

for i in data:
    if f1(i) and f2(i):
        print(sum(i))
        break