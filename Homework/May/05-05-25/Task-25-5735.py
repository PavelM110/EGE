def f(n):
    divs = set()
    cnt_2 = 0
    if n in pow_2: cnt_2 += 1
    for i in range(2, int(n ** .5) + 1):
        if n % i == 0:
            if i in pow_2 == 1:
                cnt_2 += 1
            else:
                divs.add(i)
            if n // i in pow_2 == 1:
                cnt_2 += 1
            else:
                divs.add(n // i)
    if cnt_2 >= 20:
        return sum(divs)
    return 'no'

pow_2 = [2**i for i in range(15)]

cnt = 5

for i in range(10**6 + 1, 10**20):
    s = f(i)
    if s != 'no':
        print(i, s)
        cnt -= 1
        if not cnt:
            break