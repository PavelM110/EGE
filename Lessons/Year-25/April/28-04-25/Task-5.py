cnt = 0

for n in range(1, 100_000):
    r = bin(n)[2:]
    if r.count('1') > r.count('0'):
        r += '0'
    else: r += '1'
    l = len(r)
    if l % 2 == 0:
        r = r[:(l//2)-1] + r[(l//2) + 1:]
    else:
        r = r[:(l//2) - 1] + r[(l//2)+2:]
    if not r: continue
    r = int(r, 2)
    if r == 58:
        cnt += 1

print(cnt)