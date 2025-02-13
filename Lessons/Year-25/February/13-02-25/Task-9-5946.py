with open('9_5946.txt') as file:
    data = [list(map(int, i.split())) for i in file if i]

def f1(arr):
    return len(arr) == len(set(arr))

def f2(arr):
    osts = [i % 2 for i in arr]
    return sum(osts) <= 2

cnt = 0

for i in data:
    if f1(i) and f2(i): cnt += 1

print(cnt)