with open('9_5489.txt') as file:
    data = [list(map(int, i.split())) for i in file if i]

def f1(a):
    return len(set(a)) == 5

def f2(a):
    odd = 0
    for i in a:
        if i % 2 == 0:
            odd += 1
    return odd >= 3

def f3(a):
    odd = 0
    even = 0
    for i in a:
        if i % 2 == 0: odd += i
        else: even += i
    return odd < even

cnt = 0

for n in data:
    if f1(n) and f2(n) and f3(n):
        cnt += 1

print(cnt)