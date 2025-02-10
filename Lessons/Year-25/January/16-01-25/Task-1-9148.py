from itertools import permutations

matrix = '256 1458 478 237 126 158 348 2367'.split()
graph = 'ag gx xz zd dv va ab bg bv gd ex ez ed'.split()

print(*range(1, 9))

for p in permutations('abvgdexz'):
    if all(str(p.index(x) + 1) in matrix[p.index(y)] for x, y in graph):
        print(*p)