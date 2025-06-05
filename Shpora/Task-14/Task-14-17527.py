for x in range(2030, 0, -1):
    num = 3**100 - x
    cnt = 0
    while num:
        cnt += num % 3 == 0
        num //= 3
    if cnt == 5:
        print(x)
        break