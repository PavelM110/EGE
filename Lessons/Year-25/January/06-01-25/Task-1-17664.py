from itertools import permutations

matrix = '248 157 456 136 23 34 28 17'.split()
graph = 'ch hb be ea af fc cg gd dh ab'.split()

print(*range(1, 9))
for p in permutations('abcdefgh'):
    if all(str(p.index(x) + 1) in matrix[p.index(y)] for x, y in graph):
        print(*p)
