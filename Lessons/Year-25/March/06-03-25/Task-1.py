from itertools import permutations

matrix = '26 147 456 237 37 13 245'.split()
graph = 'ae ed db bg gc ca cf fe fg'.split()

print(*range(1, 8))
for p in permutations('abcdefg'):
    if all(str(p.index(x) + 1) in matrix[p.index(y)] for x, y in graph):
        print(*p)