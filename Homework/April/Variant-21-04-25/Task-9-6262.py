with open('9_6262.txt') as file:
    data = [list(map(int, i.split())) for i in file if i]

def f1(a):
    return len(a) > len(set(a))

def f2(a):
    cnt = 0
    for i in a:
        cnt += i % 2
    return cnt == 3

cnt = 0

for i in data:
    if f1(i) ^ f2(i):
        cnt += 1

print(cnt)