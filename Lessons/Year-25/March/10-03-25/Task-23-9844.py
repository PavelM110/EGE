last_step = 0

def f(s, e, c):
    global last_step
    if s == e:
        last_step = c
        return 1
    if s < e or s == 7: return 0
    if c == 1:
        return f(s - 3, e, 2) + f(s // 2, e, 3)
    elif c == 2:
        return f(s - 1, e, 1) + f(s // 2, e, 3)
    elif c == 3:
        return f(s - 1, e, 1) + f(s - 3, e, 2)
    return f(s - 1, e, 1) + f(s - 3, e, 2) + f(s // 2, e, 3)

print(f(19, 10, 0) * f(10, 3, last_step))