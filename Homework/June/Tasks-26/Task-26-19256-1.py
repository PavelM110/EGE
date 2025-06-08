with open('26_19256 (1).txt') as file:
    n = int(file.readline())
    students = {}
    for line in file:
        i, task = map(int, line.split())
        if i in students:
            students[i] |= {task}
        else:
            students[i] = {task}

def f(student):
    if len(student) <= 1: return len(student)
    student = sorted(student)
    cnt = 1
    res = 0
    for i in range(len(student) - 1):
        if student[i+1] - student[i] == 1:
            cnt += 1
        else:
            res = max(res, cnt)
            cnt = 1
    res = max(cnt, res)
    return res

ans = [0, 0]

for i, tasks in students.items():
    t = f(tasks)
    if t > ans[1]:
        ans = [i, t]
    elif t == ans[1]:
        if ans[0] > i: ans = [i, t]

print(*ans)