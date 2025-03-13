ans = set()

def f(s, c):
    global ans
    if c == 13:
        if s < 0:
            ans.add(s)
        return 0
    f(s - 3, c + 1)
    f(s * -3, c + 1)

f(333, 0)

print(len(ans))