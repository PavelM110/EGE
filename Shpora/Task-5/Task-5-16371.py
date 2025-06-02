ans = []

for n in range(1, 10_000):
    r = bin(n)[2:]
    o = n % 3
    if o == 0:
        r += r[-2:]
    else:
        r += bin(o * 3)[2:]
    r = int(r, 2)
    if r >= 195: ans.append(r)

print(min(ans))