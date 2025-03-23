num = 15625 ** 16 - 3125**3 * 25**19 + 625**4 - 2005
cnt = 0

while num:
    if num % 5 == 0: cnt += 1
    num //= 5

print(cnt)