with open('9_18924.txt') as file:
    data = [list(map(int, i.split())) for i in file if i]

def f1(arr):
    cnt = [arr.count(i) for i in arr]
    return cnt.count(3) == 3 and cnt.count(1) == 3

def f2(arr):
    povt = [i for i in arr if arr.count(i) > 1]
    nepovt = [i for i in arr if i not in povt]
    return sum(map(lambda x: x**2, povt)) > sum(nepovt) ** 2

cnt = 0

for i in data:
    if not f1(i) and not f2(i) or (f1(i)^f2(i)):
        cnt += 1

print(cnt)