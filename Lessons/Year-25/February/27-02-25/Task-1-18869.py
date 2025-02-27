from itertools import product, permutations

matrix = '568 36 247 368 178 124 35 145'.split()
graph = 'ab bc cd de eh ha hg ga gf ef fc'.split()

print(*range(1, 9))

for p in permutations('abcdefgh'):
    if all(str(p.index(x) + 1) in matrix[p.index(y)] for x, y in graph):
        print(*p)