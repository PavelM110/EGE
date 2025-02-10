for x in range(1, 2006)[::-1]:
    num = 43**56 + 113**841 - x
    chet, nech, cnt = 0, 0, 0
    while num:
        ost = num % 4
        if ost % 2 == 0: chet += 1
        else: nech += 1
        if ost == 2: cnt += 1
        num //= 4
    if chet % 2 == 0 and nech % 2 == 0 and cnt <= 712:
        print(x)
        break