with open('26_21719.txt') as file:
    n = int(file.readline())
    data = [list(map(int, i.split())) for i in file if i]

def f(student):
    if len(student) <= 1: return len(student)
    student = sorted(student)
    res = 0
    cnt = 1
    for i in range(len(student) - 1):
        if student[i+1] - student[i] == 2:
            cnt += 1
        else:
            res = max(res, cnt)
            cnt = 1
    res = max(res,cnt)
    return res

studens = [set() for i in range(1_000_001)]

for i, t in data:
    studens[i] |= {t}

print(studens.index(max(studens, key=len)))

for i in range(len(studens)):
    studens[i] = f(studens[i])

print(studens[18317])

ans = max(studens)

for i in range(len(studens)):
    if studens[i] == ans:
        print(i, studens[i])
        break