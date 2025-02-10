from itertools import product, permutations

matrix = '347 3456 1245 1237 236 25 14'.split()
graph = 'ba ad df fg ge ec cb ca cd ed ef'.split()

print(*range(1, 8))
for p in permutations('abcdefg'):
    if all(str(p.index(x) + 1) in matrix[p.index(y)] for x, y in graph):
        print(*p)