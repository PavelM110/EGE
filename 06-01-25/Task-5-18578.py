def f(num):
    res = ''
    while num:
        res += str(num % 4)
        num //= 4
    return res[::-1]

for n in range(1, 10_000)[::-1]:
    r = f(n)
    if n % 4 == 0:
        r = '2' + r + '03'
    else:
        r += f((n % 4) * 5)
    r = int(r, 4)
    if r <= 567:
        print(n)
        break