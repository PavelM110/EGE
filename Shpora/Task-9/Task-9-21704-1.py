with open('9_21704 (1).txt') as file:
    data = [list(map(int, i.split())) for i in file if i]

def f1(a):
    return all(a[i] > a[i+1] for i in range(len(a) - 1))

def f2(a):
    return (min(a) + max(a)) / 2 > (sum(a) - min(a) - max(a)) / (len(a) - 2)

for a in data:
    if f1(a) and f2(a):
        print(sum(a))
        break