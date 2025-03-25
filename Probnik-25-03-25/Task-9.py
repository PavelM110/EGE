with open('904.txt') as file:
    data = [list(map(int, i.split())) for i in file if i]

def f1(arr):
    cnt = [arr.count(i) for i in set(arr)]
    return cnt.count(2) == 1 and cnt.count(1) == 5

def f2(arr):
    povt = [i for i in arr if arr.count(i) > 1]
    nepovt = [i for i in arr if arr.count(i) == 1]
    povt = sum(povt) ** 2
    nepovt = sum(nepovt) ** 2
    return povt > nepovt

for i in data:
    if f1(i) and f2(i):
        print(sum(i))
        break
