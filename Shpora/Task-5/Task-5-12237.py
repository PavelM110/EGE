ans = []

for n in range(1, 10_000):
    r = bin(n)[2:]
    if r[-1] == '0': r += r[-2:]
    else: r = '1' + r + '0'
    r = int(r, 2)
    if r < 100: ans.append(n)

print(max(ans))