from itertools import permutations

matrix = '346 45 16 12567 24 1347 46'.split()
graph = 'ab bv vg gd de eb bx xa bd vd'.split()

print(*range(1, 8))

for p in permutations('abvgdex'):
    if all(str(p.index(x) + 1) in matrix[p.index(y)] for x, y in graph):
        print(*p)