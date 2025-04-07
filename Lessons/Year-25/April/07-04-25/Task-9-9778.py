with open('09_9778.txt') as file:
    data = [list(map(int, i.split())) for i in file if i]

def f1(arr):
    return len(set(arr)) == 5

def f2(arr):
    povt = [i for i in arr if arr.count(i) == 2][0]
    nep = sum(arr) - povt * 2
    return povt >= nep / 4

for n, i in enumerate(data, 1):
    if f1(i) and f2(i):
        print(n)
        break