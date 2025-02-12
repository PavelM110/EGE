with open('9_11946.txt') as file:
    data = [list(map(int, i.split())) for i in file if i]

def f1(arr):
    count = [arr.count(i) for i in arr]
    return count.count(3) == 3 and count.count(1) == 4

def f2(arr):
    return arr == sorted(arr)

cnt = 0

for i in data:
    if (f1(i) ^ f2(i)) or (not f1(i) and not f2(i)): cnt += 1

print(cnt)
