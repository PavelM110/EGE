from itertools import permutations

graph = 'ab bd de ez zx xv vg ga ad gd vz'.split()
matrix = '245 15 478 135 1246 58 38 367'.split()

print(*range(1, 9))
for p in permutations('abvgdexz'):
    if all(str(p.index(x) + 1) in matrix[p.index(y)] for x, y in graph):
        print(*p)