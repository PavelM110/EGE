with open('9_4589.txt') as file:
    data = [list(map(int, i.split())) for i in file if i]

def f1(arr):
    return max(arr) < sum(arr) - max(arr)

def f2(arr):
    return max(arr) + min(arr) == sum(arr) - max(arr) - min(arr)

cnt = 0

for i in data:
    if f1(i) and f2(i):
        cnt += 1

print(cnt)