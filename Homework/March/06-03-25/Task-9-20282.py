with open('9.15_20282.txt') as file:
    data = [list(map(int, i.split())) for i in file]

def f1(arr):
    cnt = [arr.count(i) for i in set(arr)]
    return cnt.count(3) == 1 and cnt.count(1) == 3

def f2(arr):
    maxx = max(arr)
    minn = min(arr)
    summ = (sum(arr) - maxx - minn) ** 2
    sum1 = maxx ** 2 + minn ** 2
    return sum1 >= summ

cnt = 0

for i in data:
    if f1(i) and f2(i): cnt += 1

print(cnt)