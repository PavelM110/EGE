def fu(x, y, z, w):
    return (not(w <= z)) or (x <= y) or (not x)

print('x y z w')

for x in (0, 1):
    for y in (0, 1):
        for z in (0, 1):
            for w in (0, 1):
                f = fu(x, y, z, w)
                if not f:
                    print(x, y, z, w)