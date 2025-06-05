num = 2 * 729**333 + 2 * 243**334 - 81**335 + 2 * 27**336 - 2 * 9**337 - 338

cnt = 0

while num:
    cnt += num % 9 != 0
    num //= 9

print(cnt)