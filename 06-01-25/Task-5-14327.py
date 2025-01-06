for n in range(1, 10_000)[::-1]:
    r = oct(n)[2:]
    if n % 2 == 0:
        r += str(max([int(i) for i in '01234567' if i in r]))
    else:
        r += oct(min([int(i) for i in '01234567' if i in r]) * 2)[2:]
    r = int(r, 8)
    if r < 313:
        print(n)
        break