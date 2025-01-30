def f(n):
    res = ''
    while n:
        res += str(n % 3)
        n //= 3
    return res[::-1]

ans = []

for n in range(1, 1000):
    r = f(n)
    if sum(map(int, r)) % 3 == 0:
        r += '212'
    else:
         r += f(sum(map(int, r)) * 2)
    r = int(r, 3)
    if r > 490: ans.append(r)

print(min(ans))