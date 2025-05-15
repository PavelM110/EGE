from itertools import permutations

matrix = '3578 346 1258 26 13 248 18 1367'.split()
graph = 'ab bd dg gx xz ze ev va bv ed dx ex'.split()

print(*range(1, 9))

for p in permutations('abvgdexz'):
    if all(str(p.index(x) + 1) in matrix[p.index(y)] for x, y in graph):
        print(*p)