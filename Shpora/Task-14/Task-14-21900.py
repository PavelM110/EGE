for x in range(1, 2301)[::-1]:
    num = 7**350 + 7**150 - x
    cnt_0 = 0
    while num:
        cnt_0 += num % 7 == 0
        num //= 7
    if cnt_0 == 200:
        print(x)
        break