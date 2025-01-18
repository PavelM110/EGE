with open('09_10910.txt') as file:
    data = [list(map(int, i.split())) for i in file if i]

def f1(arr):
    return(arr.count(min(arr)) == 1)

def f2(arr):
    return(len(arr) != len(set(arr)))

def f3(arr):
    povt = [i for i in arr if arr.count(i) > 1]
    return((max(arr) + min(arr)) < sum(povt))

cnt = 0

for i in data:
    if f1(i) and f2(i) and f3(i):
        cnt += 1

print(cnt)