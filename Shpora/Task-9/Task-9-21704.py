with open('9_21704.txt') as file:
    data = [list(map(int, i.split())) for i in file if i]

def f1(a):
    return all(a[i] > a[i + 1] for i in range(len(a) - 1))

def f2(a):
    a = sorted(a)
    return (a[0] + a[-1]) / 2 > sum(a[1:-1]) / 5

for i in data:
    if f1(i) and f2(i):
        print(sum(i))
        break