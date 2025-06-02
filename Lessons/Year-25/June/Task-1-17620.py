from itertools import permutations

matrix = '256 134 267 27 16 135 34'.split()
graph = 'af fe ec cg gd db ba fb ed'.split()

print(*range(1, 8))

for p in permutations('abcdefg'):
    if all(str(p.index(x) + 1) in matrix[p.index(y)] for x, y in graph):
        print(*p)