ans = []

for n in range(1, 10_000):
    r = bin(n)[2:]
    r += str(sum(map(int, r)) % 2)
    r += str(sum(map(int, r)) % 2)
    r = int(r, 2)
    if r > 75: ans.append(r)

print(min(ans))