from itertools import permutations

graph = 'AD DE EG GC CF FA AB BE FB'.split()
matrix = '37 367 125 56 34 247 126'.split()

print(*range(1, 8))

for p in permutations('ABCDEFG'):
    if all(str(p.index(x) + 1) in matrix[p.index(y)] for x, y in graph):
        print(*p)