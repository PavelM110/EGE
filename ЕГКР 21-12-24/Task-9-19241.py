with open('input.txt') as file:
    data = [list(map(int, i.split())) for i in file if i]

def f1(arr):
    cnt = sorted([arr.count(i) for i in set(arr)])
    return cnt == [1, 3, 3]

def f2(arr):
    povt = [i for i in set(arr) if arr.count(i) > 1]
    nepovt = [i for i in set(arr) if arr.count(i) == 1]
    return(sum(nepovt) > sum(povt) / 2)

for pos, arr in list(enumerate(data, start=1))[::-1]:
    if f1(arr) and f2(arr):
        print(pos)
        break