from itertools import permutations

matrix = '56 378 26 68 17 134 258 247'.split()
graph = 'ac cf fd dh hg ga ab bc be ed'.split()

print(*range(1, 9))

for p in permutations('abcdefgh'):
    if all(str(p.index(x) + 1) in matrix[p.index(y)] for x, y in graph):
        print(*p)