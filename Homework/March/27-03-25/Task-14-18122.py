for x in range(1, 5556)[::-1]:
    num = 5**150 + 5**135 - x
    cnt = 0
    while num:
        cnt += 1 if num % 5 == 4 else 0
        num //= 5
    if cnt == 134:
        print(x)
        break