for x in range(1, 2031):
    num = 6**260 + 6**160 + 6**60 - x
    cnt = 0
    while num:
        cnt += num % 6 == 0
        num //= 6
    if cnt == 202:
        print(x)
        break