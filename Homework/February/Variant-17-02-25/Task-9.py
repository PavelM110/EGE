with open('9.txt') as file:
    data = [list(map(int, i.split())) for i in file if i]

def f1(arr):
    cnt = [arr.count(i) for i in set(arr)]
    u = cnt.count(3) == 1 and cnt.count(1) == 4
    return u

def f2(arr):
    osts = [i % 2 for i in arr]
    return sum(osts) <= 3

cnt = 0

for i in data:
    if f1(i) and f2(i): cnt += 1

print(cnt)