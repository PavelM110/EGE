for n in range(2, 10000):
    r = bin(n)[2:]
    ch_1 = 0
    n_0 = 0
    for p in range(0, len(r), 2):
        if r[p] == '0': n_0 += 1
    for p in range(1, len(r), 2):
        if r[p] == '1': ch_1 += 1
    r = abs(ch_1 - n_0)
    if r == 5:
        print(n)
        break