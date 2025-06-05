with open('26_19256 (1).txt') as file:
    n = int(file.readline())
    data = [list(map(int, i.split())) for i in file if i]

def f(student):
    if len(student) <= 1: return len(student)
    student = sorted(student)
    res = 0
    cnt = 0
    for i in range(len(student) - 1):
        if student[i+1] - student[i] == 1:
            cnt += 1
        else:
            res = max(res, cnt)
            cnt = 0
    if student[-1] - student[-2] == 1: cnt += 1
    res = max(res, cnt)
    return res

data = sorted(data)

students = [set() for i in range(data[-1][0] + 1)]

for s, n in data:
    students[s] |= {n}

for i in range(len(students)):
    students[i] = f(students[i])

print(students.index(max(students)), max(students))