from itertools import permutations

matrix = '256 135 2457 37 1236 157 346'.split()
graph = 'av vg gd db bx xa az zv zg zd dx'.split()

for p in permutations('abvgdxz'):
    if all(str(p.index(x) + 1)in matrix[p.index(y)] for x, y in graph):
        print(*p)