for n in range(10_000, 100_000):
    nums = sorted(list(map(int, [i for i in str(n)])))
    suma = (nums[0] + nums[-1]) ** 2
    chet = [int(i) for i in str(n) if int(i) % 2 == 0]
    prod = 1
    for i in chet:
        prod *= i
    res = str(max(prod, suma)) + str(min(prod, suma))
    if res == ('12116'):
        print(n)
        break