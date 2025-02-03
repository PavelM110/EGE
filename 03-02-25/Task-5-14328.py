from string import digits, ascii_lowercase

alph = digits + ascii_lowercase

def f(n, sys):
    res = ''
    while n:
        res += alph[n % sys]
        n //= sys
    return res[::-1]

res = []

for n in range(0, 1000):
    r = f(n, 12)
    if n % 3 == 0: r = '1' + r + 'b'
    else: r = '2' + r + '0'
    r = int(r, 12)
    if r < 1996:
        res.append(r)

print(min(res))