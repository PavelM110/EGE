from itertools import product, permutations

def f(x, y, z, w):
    return((y <= x) and (not z) and w)

print('x y z w F')

for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if f(x, y, z, w):
                    print(x, y, z, w, int(f(x, y,z, w)))