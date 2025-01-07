from itertools import permutations

matrix = '234 156 17 15 246 257 36'.split()
graph = 'fe ed dc cb bg gf ag ab ad'.split()

print(*range(1, 8))
for p in permutations('abcdefg'):
    if all(str(p.index(x) + 1) in matrix[p.index(y)] for x, y in graph):
        print(*p)