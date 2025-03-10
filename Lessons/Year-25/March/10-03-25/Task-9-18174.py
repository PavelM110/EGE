with open('9_18174 (1).txt') as file:
    data = [list(map(int, i.split())) for i in file if i]

def f1(arr):
    cnt = [arr.count(i) for i in set(arr)]
    return cnt.count(2) == 1 and cnt.count(1) == 4

def f2(arr):
    summ_pos = sum(i for i in arr if i > 0)
    summ_neg = abs(sum( i for i in arr if i < 0))
    return summ_neg > summ_pos

cnt = 0

for i in data:
    if f1(i) and f2(i):
        cnt += 1

print(cnt)