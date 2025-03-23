with open('9_17628.txt') as file:
    data = [list(map(int, i.split())) for i in file if i]

def f1(arr):
    u = (max(arr) + min(arr)) <= (sum(arr) - (max(arr) + min(arr)))
    return u

cnt = 0

print(data[:5])

for i in data:
    if f1(i):
        cnt += 1

print(cnt)