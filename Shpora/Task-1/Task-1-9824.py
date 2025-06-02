from itertools import permutations

matrix = '346 45 16 125 247 137 56'.split()
graph = 'df fa ab cb ce eg gd de ca'.split()

print(*range(1, 8))

for p in permutations('abcdefg'):
    if all(str(p.index(x) + 1) in matrix[p.index(y)] for x, y in graph):
        print(*p)