from itertools import permutations

matrix = '234 136 12 157 467 25 45'.split()
graph = 'fb bd da ae ec cg gf fd ge'.split()

print(*range(1, 8))

for p in permutations('abcdefg'):
    if all(str(p.index(x) + 1) in matrix[p.index(y)] for x, y in graph):
        print(*p)