from itertools import permutations

matrix = '356 358 128 67 127 147 456 23'.split()
graph = 'ab bd dx xz ze eg gv va vb gd ex'.split()

print(*range(1, 9))
for p in permutations('abvgdexz'):
    if all(str(p.index(x) + 1) in matrix[p.index(y)] for x, y in graph):
        print(*p)