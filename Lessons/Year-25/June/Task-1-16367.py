from itertools import permutations

matrix = '246 16 57 15 347 127 356'.split()
graph = 'ef fd dc ca ag gb be fc ba'.split()

print(*range(1, 8))

for p in permutations('abcdefg'):
    if all(str(p.index(x) + 1) in matrix[p.index(y)] for x, y in graph):
        print(*p)