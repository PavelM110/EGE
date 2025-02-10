def f(a, b, c, d):
    return((not a) and (not b)) or (b == c) or d

print('a b c d F')

for a in (1, 0):
    for b in (1, 0):
        for c in (1, 0):
            for d in (1, 0):
                f = f(a, b, c, d)
                if not f: # если нужны 0
                    print(a, b, c, d)

                if f: # если нужны 1
                    print(a, b, c, d)