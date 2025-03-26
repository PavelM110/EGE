ans = []

for x in range(1, 2031):
    num = 2**2025 + 2**2024 - 2**2021 - x
    cnt = 0
    while num:
        if num % 4 == 0: cnt += 1
        num //= 4
    ans.append((cnt, x))

print(sorted(ans, key=lambda x: (-x[0], -x[1])))