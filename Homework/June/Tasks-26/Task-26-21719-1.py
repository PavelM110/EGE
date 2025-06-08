with open('26_21719.txt') as file:
    n = int(file.readline())
    students = {}
    for student in file:
        i, task = map(int, student.split())
        if i in students: students[i] |= {task}
        else: students[i] = {task}

def f(tasks):
    if len(tasks) <= 1: return len(tasks)
    cnt = 1
    res = 0
    tasks = sorted(tasks)
    for i in range(len(tasks) - 1):
        if tasks[i + 1] - tasks[i] == 2:
            cnt += 1
        else:
            res = max(res, cnt)
            cnt = 1
        res = max(res, cnt)
    return res

ans = [0, 0]

for i, tasks in students.items():
    t = f(tasks)
    if t > ans[0]: ans = [t, i]
    elif t == ans[0]:
        if ans[1] > i: ans = [t, i]

print(ans[1], ans[0])