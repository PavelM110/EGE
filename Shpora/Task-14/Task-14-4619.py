num = 343 ** 1515 - 6*49 ** 1520 + 5*49**1510 - 3*7 ** 1530 - 1550

cnt = 0

while num:
    cnt += num % 7 == 0
    num //= 7

print(cnt)