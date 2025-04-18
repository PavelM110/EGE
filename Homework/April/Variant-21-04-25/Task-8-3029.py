from itertools import product

cnt = 0

def f(n):
    for i in range(len(n) - 2):
        st = n[i:i+3]
        if len(set(st)) == 1: return False
    return True


for i in product('012345678', repeat=7):
    i = ''.join(i)
    if i[0] != '0' and i[-1] not in '347':
        if f(i): cnt += 1

print(cnt)