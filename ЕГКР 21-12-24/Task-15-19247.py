for a in range(1, 1000):
    if all((((x - 3 * y) < a) or (y > 400) or (x > 56)) for x in range(1, 1_000) for y in range(1, 1_000)):
        print(a)
        break