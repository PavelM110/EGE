from itertools import permutations

matrix = '234 157 147 138 268 58 23 456'.split()
graph = 'bd dg ga af fh hc cb be ed eh gf'.split()

print(*range(1, 9))

for p in permutations('abcdefgh'):
    if all(str(p.index(x) + 1) in matrix[p.index(y)] for x, y in graph):
        print(*p)