for x in range(2030, 0, -1):
    num = 7**91 + 7**160 - x
    cnt = 0
    while num:
        cnt += num % 7 == 0
        num //= 7
    if cnt == 70:
        print(x)
        break