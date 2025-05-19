for x in range(1, 10_001)[::-1]:
    num = 6**900 + 6**10 - x
    cnt_3, cnt_5 = 0, 0
    while num:
        cnt_3 += num % 6 == 3
        cnt_5 += num % 6 == 5
        num //= 6
    if cnt_3 == cnt_5:
        print(x)
        break